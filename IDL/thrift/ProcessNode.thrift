include "Common.thrift"


service processNode {
	returnInfo getProcessInfo (1: Common.empty req)
	returnInfo getVersionInfo (1: Common.empty req)
	returnInfo stopProcess (1: requestInfo req)
	returnInfo startProcess (1: requestInfo req)
	returnInfo killMainProcess (1: Common.empty req)
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
