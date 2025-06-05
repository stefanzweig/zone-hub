// Version = 1.0.20220131
include "Common.thrift"


service someIpNode {
	// 开启 SomeIp 协议栈 修改入参
	Common.result startSomeIpStack (1: Common.netInfo req)
	// 开启 SomeIp 协议栈 修改入参
	// 2023年5月4日 废弃 该功能移到 TCPIPNode 中
	Common.result startSomeIpStackBypass (1: Common.empty req)
	// 停止 SomeIp 协议栈 修改入参
	Common.result stopSomeIpStack (1: Common.netInfo req)
	// 停止 SomeipStackBypass 协议栈
	// 2023年5月4日 废弃 该功能移到 TCPIPNode 中
	Common.result stopSomeIpStackBypass (1: Common.empty req)
	// 添加 SomeIpArxml 修改入参
	Common.result addSomeIpArxml (1: addSomeipArxmlRequest req)
	// 添加网卡信息，仅给界面调用 修改入参
	Common.result addIfaceInfo (1: Common.netInfo req)
	// 获取网卡信息，仅给界面调用 修改入参
	Common.netInfo getIfaceInfo (1: Common.netInfo req)
	// 获取后台正在使用的 Arxml dict 修改返回
	someipArxmlJson getArxmlToJson (1: Common.netInfo req)
	// 更新 Someip service 的配置信息 修改入参
	Common.result updateSomeipServiceConfig (1: serviceTag req)
	// 复位
	Common.result reset ()
	// 同步发送Someip Call 不需要修改数据结构，但是需要修改逻辑，在 client 端的 someipPackage 中添加 channel 的信息
	someipResponseContext someipCallSync (1: someipCallContext req)
	// 获取 Someip 协议栈状态 修改入参
	Common.result getSomeipStackStatus (1: Common.netInfo req)
	// 获取所有 SomeipStack Status 的状态 新增函数，需要实现
	someipStackConfig getAllSomeipStackConfig (1: Common.empty req)
	// 获取当前网段存在的服务 修改入参
	someipServiceInfos getAllOfferService (1: Common.netInfo req)
	// 获取当前服务状态列表 修改入参
	serviceStates getServiceStates (1: Common.netInfo req)
	// 启动数据录制 修改入参
	Common.result startLog (1: logRequest req)
	// 停止数据录制 修改入参
	Common.result stopLog (1: logRequest req)
	// 获取当前数据记录任务的状态 修改入参
	Common.result getLogStatus (1: logRequest req)
	// 转换 SomeipDB 文件到 Json
	Common.result convertSomeipDbToJson (1: convertInput req)
	// 转换 SomeipDB 文件到 Py
	Common.result convertSomeipDbToPy (1: convertInput req)
	// 一键设置一个通道的 SomeipConfig
	Common.result setAllSomeipStackConfig (1: someipStackConfig req)
	//Someip message发送相关函数
	Common.result someipPublish(1: someipPackage req)
	Common.result someipSetDefaultAnswer(1: someipPackage req)
	Common.result someipCallAsync(1: someipPackage req)
}
struct someipInfo {
	1: Common.result result
	2: string jsonStrInfo
}
struct serviceTag {
	1: string serviceName
	2: i32 instanceId
	3: string serviceType
	4: bool serviceState
	5: i32 channel
	6: i32 useType
}
struct someipCallContext {
	2: i32 timeout
	1: string strContext
	3: i32 channel
}
struct someipResponseContext {
	1: Common.result result
	2: string strContext
}
struct someipServiceInfo {
	1: string serviceName
	2: i64 serviceId
	3: i32 instanceId
	4: string srcIp
}
struct someipServiceInfos {
	1: Common.result result
	2: list<someipServiceInfo> infos
}
struct someipArxmlJson {
	1: i32 result
	2: string reason
	3: string jsonData
}
struct convertInput {
	1: string srcFile
	2: string dstFile
}
struct serviceState {
	1: string serviceName
	2: i32 serviceId
	3: i32 instanceId
	4: bool serviceState
	5: string serviceSide
	6: i32 channel
}
struct serviceStates {
	1: Common.result result
	2: list<serviceState> serviceStates
}
// + type
struct someipChannelConfig {
	1: Common.netInfo netInfo
	2: list<string> arxmlPaths
	3: Common.eTHDEVICE ethDevice
}
struct someipStackConfig {
	1: Common.result result
	2: list<someipChannelConfig> configs
	3: list<Common.arpPair> arpPairs
}
struct logRequest {
	1: Common.netInfo netInfo
	2: Common.folderFilePath path
}
struct addSomeipArxmlRequest {
	1: Common.filePath filePath
	2: i32 channel
}
struct someipPackage {
    1: string serviceName
    2: string srcIp
    3: i32 srcPort
    4: string destIp
    5: i32 destPort
    6: string interfaceType
    7: i32 serviceId
    8: i32 instanceId
    9: i32 interfaceId
    10: string interfaceName
    11: string context
    12: string payload
    13: i32 msgType
    14: i32 retCode
    15: i32 sessionId
    16: i32 channel
    17: i32 time
    18: i32 deltaTime
	19: string by
}
