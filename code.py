import time

start_time = time.time()
time.sleep(3)
end_time = time.time()


print('Time Taken:', time.strftime("%H hours, %M Minutes and %S seconds", time.gmtime(end_time - start_time)))


"""
We have a system where products can be placed into catalogs and buyers are assigned to a catalog.
Products can have different visibility settings. If the visibility setting is “default” then any buyer can
see the product. If the visibility is “catalog_members” then only buyers who are a member of a catalog
including the product can see it. A query for products on behalf of a buyer should return any product
that has visibility “default” OR the product exists in a catalog that includes the buyer. A product has a
name, price, and visibility setting.

a) How would you model these relationships?
b) How would you write a SQL query to return the list of products?
"""

"""
A) First, we need a Product Model, later we need a Catalog Model, that you can link or do a ForeignKey to Buyer Model, and we need
another FK to products.
I think Buyer is a User based Model, if visibility is default in that catalog, we can show the catalog in the UI for all users but
we need implement the query to get just all the visibility="default" query or ORM example:

# I skip the pagination for now, like a "Proof of Concept"
catalogs = Catalog.objects.filter("visibility="default").values("name", "description")

# this is similar to:
SELECT name, description FROM catalogs WHERE catalogs.visibility == "default";

But if the catalog has "catalog_members" visibility, we need filter the list of catalogs of the user
Example:

user_catalogs = request.user.catalogs.filter(visibility="catalog_members")

# We need do a for loop, to print it of transform it into a JsonResponse if we need a quick api

for use_catalog in user_catalogs:
  print(user_catalog.name)
  print(user_catalog.description)
"""

