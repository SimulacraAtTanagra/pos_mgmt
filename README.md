## The purpose of this project is as follows:
This program procedurally generates documentation relating to position management, increasing data freshness.
## Here's some back story on why I needed to build this:
Currently, we manage CUNYfirst HCM position numbers through a report directly from the system, which has the limitation of being needlessly effortful, partially duplicating other work, and resulting in stale data. This process leverages other data sources that we refresh more frequently for other reasons, effectively increasing the benefit without additional effort.
## This project leverages the following libraries:
pandas, fuzzywuzzy
## In order to use this, you'll first need do the following:
The user will need to configure this by defining the locations where a Current Job Report will be (a static location which has data to be updated), and a location to drop the data off when it is complete. 
## The expected frequency for running this code is as follows:
Daily