include "CommonNode.thrift"


service processNode {
	returnInfo getProcessInfo ()
	returnInfo getVersionInfo ()
	returnInfo stopProcess (1: requestInfo req)
	returnInfo startProcess (1: requestInfo req)
	returnInfo killMainProcess ()
	returnInfo processLogConfig (1: requestInfo req)
}
struct returnInfo {
	1: string info
	2: i32 status
}
struct requestInfo {
	1: string process
	2: string loglevel
}
