import sys, action, status, helpers, optimizeBatch
import Batch
# new imports start here

# settings = helpers.get_settings()

try:
	action = str(sys.argv[1])
except:
	action = None
try:
	PATH = str(sys.argv[2])
except:
	PATH = None

if action == 'status' or action == None:
	status.execute()

elif action == '-o':
	optimizeBatch.execute(PATH)

elif action == "batch":
    Batch.execute()
# new actions start here
