# factory example - moving a Django model
Demo Django project used to show how to move a model from its original app to a new app.

**Migrating a model between apps.**

The short answer is, *don't do it!!*

But that answer rarely works in the real world of living projects and production databases. Therefore, I have created a [sample GitHub repo][1] to demonstrate this rather complicated process.

I am using MySQL. *(No, those aren't my real credentials).*

**The Problem**

The example I'm using is a factory project with a **cars** app that initially has a `Car` model and a `Tires` model. 

    factory
      |_ cars
        |_ Car
        |_ Tires

The `Car` model has a ForeignKey relationship with `Tires`. (As in, you specify the tires via the car model). 

However, we soon realize that `Tires` is going to be a large model with it's own views, etc., and therefore we want it in its own app. The desired structure is therefore:

    factory
      |_ cars
        |_ Car
      |_ tires
        |_ Tires

And we need to keep the ForeignKey relationship between `Car` and `Tires` because too much depends on preserving the data.

**The Solution**

**Step 1.** Setup initial app with bad design.

Browse through the code of [step 1.][2]

**Step 2.** Create an admin interface and add a bunch of data containing ForeignKey relationships. 

View [step 2.][3]

**Step 3.** Decide to move the `Tires` model to its own app. Meticulously cut and paste code into the new tires app. Make certain you update the `Car` model to point to the new `tires.Tires` model.

Then run `./manage.py makemigrations` and backup the database somewhere (just in case this fails horribly).

Finally, run `./manage.py migrate` and see the error message of doom,

**django.db.utils.IntegrityError: (1217, 'Cannot delete or update a parent row: a foreign key constraint fails')**

View code and migrations so far in [step 3.][4]

**Step 4.** The tricky part. The auto-generated migrations fail to see that you've merely copied a model to a different app. So, we have to do a number of things to remedy this.

You can follow along and view the final migrations with comments in [step 4.][5] I did test this to verify it works. 

First, we are going to work on `cars`. You have to make a new, empty migration. This migration actually needs to run before the most recently created migration (the one that failed to execute), so I renumbered the one I created, and changed the dependencies to execute my custom migration, and then the last auto-generated migration for the `cars` app.

You can create an empty migration with:

    ./manage.py makemigrations --empty cars

**Step 4.a.** Make custom *old_app* migration.

In this first custom migration, I'm going to do only  a "database_operations" migration. Django gives you the option to split "state" and "database" operations. You can see how this is done by viewing the [code here][6].

My goal in this first step is to rename the database tables from `oldapp_model` to `newapp_model` without messing with Django's state. You kind of have to figure out what Django would have named your database table based on the app name and model name. 

Now, you are ready to modify the initial `tires` migration.

**Step 4.b.** Modify *new_app* initial migration

The operations are fine, but we want to only modify the "state" and not the database. Why? Because we are actually keeping the database tables from the `cars` app. Also, you need to make sure that the previously made custom migration is a dependency of this migration. See the tires [migration file][7].

So, now we have renamed `cars.Tires` to `tires.Tires` in the database, and changed the Django state to recognize the `tires.Tires` table. 

**Step 4.c.** Modify *old_app* last auto-generated migration.

Going *back* to cars, we need to modify that last auto-generated migration. It should require our first custom cars migration, and the initial tires migration (that we just modified). 

Here we should leave the `AlterField` operations because the `Car` model *is pointing* to a different model (even though it has the same data). However, we need to remove the lines of migration about `DeleteModel` because the `cars.Tires` model no longer exists. It has been fully converted into `tires.Tires`. View [this migration][8].

**Step 4.d.** Clean up stale model in *old_app*.

Last, but not least, you need to make one last custom migration in the cars app. Here, we will do a "state" operation only to delete the `cars.Tires` model. It is state-only because the database table for `cars.Tires` has already been renamed. This [last migration][9] cleans up the remaining Django state.


  [1]: https://github.com/halfnibble/factory
  [2]: https://github.com/halfnibble/factory/tree/step1
  [3]: https://github.com/halfnibble/factory/tree/step2
  [4]: https://github.com/halfnibble/factory/tree/step3
  [5]: https://github.com/halfnibble/factory/tree/step4
  [6]: https://github.com/halfnibble/factory/blob/step4/cars/migrations/0002_auto_20150603_0642.py
  [7]: https://github.com/halfnibble/factory/blob/step4/tires/migrations/0001_initial.py
  [8]: https://github.com/halfnibble/factory/blob/step4/cars/migrations/0003_auto_20150603_0630.py
  [9]: https://github.com/halfnibble/factory/blob/step4/cars/migrations/0004_auto_20150603_0701.py
