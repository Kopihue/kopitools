from kopilogs import paint
from kopilogs import log, Log

Log.icons = True

log("SUCCESS").success()
log("CRITICAL").critical()
log("UNKNOWN").unknown()
