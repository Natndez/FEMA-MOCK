### FEMA Mock Application
<p>FEMA is a government organization that aids in natural disasters. A few years ago there was a catastrophic<br>
hurricane that damaged the lives of many people. FEMA was able to raise a lot of volunteers to help handle the<br>
damage. There was an issue however, while they had a lot of help, FEMA did not have a way to assign various jobs<br>
to the volunteers. I figured it would be a good coding challenge to create a "mock website" for them that could be able<br>
to help spread the workload.<br></p>




* - Ideal features

| Technologies |
-Flask can't decide
-Perhaps nodeJS or Python with Flask for the backend
-Chrome Dev Tools ( The best dev tools :) )

| FEMA | (6-8 hours... need to learn about databases)
-Input items/jobs into database
-3 databases, items, jobs, and commitments
-Government organization
-Perhaps they should "sign in" if they are an employee

| Distribution Center | (4 Hours)
-Look at items and agree which items to take
-Have providers in the distribution center. 
-Distribution center does not have constant inventory, just donations that come and go.
-Have a "ledger" of what donations are present
-When the donations of the essential items (e.g. water, food, clothes, materials to rebuild)
-Have the ability to make a new distribution *

| Drivers | (1 Hour)
-Take items to commitments
-Paid position

| Workers | (1 Hour)
-Jobs go to workers
-Volunteers

| Items | (30 mins - 1 Hour)
-Items that are in the warehouse

| Jobs | (2 Hours)
-List of jobs that need posting
-Have a tally of how many positions are in each location

| Commitments | (1-2 Hours)
-Things that have been committed to be donated but are en route (i.e. someone said they will donate 30 shirts but it'll take time to ship)
-Maybe can be lost in transit? Or maybe not that deep.

| Technical Requirements | (Figuring out how to set each thing up with these requirements will take more time for me...)
-Must be hosted so the site can actually be accessed and save state or something
-Figure out how to set up a "Server"
-May have to grind the odin project to complete this
-Can be one app with multiple different views instead of creating multiple apps that have access to the same database
-Try to have either a log in or just a registration that adds someone to their specific department (e.g. worker, driver, donations, etc.)
-ALL positions must be registered, including the distribution center.


