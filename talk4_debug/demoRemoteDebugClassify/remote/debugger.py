import logging
logging.basicConfig(
        filename = f"{__name__}.log",
        level=logging.INFO,
        format = "%(asctime)s [%(levelname)s] %(name)s: %(message)s"
)
debugLog = logging.getLogger(__name__)



# base directory of installed (system) python
PYTHON_BASEDIR = r"C:\Users\Tinitun\AppData\Local\Programs\Python\Python37-32"
PYTHON_EXE = rf"{PYTHON_BASEDIR}\python.exe"  # global python executable
DEBUG_PORT = 2633

def startDebug():
	try:
		import debugpy
	except ImportError as exc:
		#print(f"Error. {exc}")
		debugLog.exception("Debugpy not imported")

	try:
		alreadyConnected = debugpy.is_client_connected()
		if not alreadyConnected:
			debugpy.log_to(r"C:\logDebugpy")
			debugLog.info("Saving debugpy logs in log directory")
			debugpy.configure(python=PYTHON_EXE)
			debugLog.info(f"External Python assigned to {PYTHON_EXE}")
			debugpy.listen(("0.0.0.0", DEBUG_PORT))
			debugLog.info(f"Listening in port {DEBUG_PORT}")
			debugpy.wait_for_client()
			debugLog.info("Continued after wairting for client")
		else:
			debugLog.warning("Debug session already connected.")
	except Exception as exc:
		debugLog.exception("Something went wrong")
