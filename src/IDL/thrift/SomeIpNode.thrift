// Version = 1.0.20220131
include "CommonNode.thrift"


service someIpNode {
	// 开启 SomeIp 协议栈 修改入参
	CommonNode.result startSomeIpStack (1: CommonNode.netInfo req)
	// 开启 SomeIp 协议栈 修改入参
	// 2023年5月4日 废弃 该功能移到 TCPIPNode 中
	CommonNode.result startSomeIpStackBypass (1: CommonNode.empty req)
	// 停止 SomeIp 协议栈 修改入参
	CommonNode.result stopSomeIpStack (1: CommonNode.netInfo req)
	// 停止 SomeipStackBypass 协议栈
	// 2023年5月4日 废弃 该功能移到 TCPIPNode 中
	CommonNode.result stopSomeIpStackBypass (1: CommonNode.empty req)
	// 添加 SomeIpArxml 修改入参
	CommonNode.result addSomeIpArxml (1: addSomeipArxmlRequest req)
	// 添加网卡信息，仅给界面调用 修改入参
	CommonNode.result addIfaceInfo (1: CommonNode.netInfo req)
	// 获取网卡信息，仅给界面调用 修改入参
	CommonNode.netInfo getIfaceInfo (1: CommonNode.netInfo req)
	// 获取后台正在使用的 Arxml dict 修改返回
	someipArxmlJson getArxmlToJson (1: CommonNode.netInfo req)
	// 更新 Someip service 的配置信息 修改入参
	CommonNode.result updateSomeipServiceConfig (1: serviceTag req)
	// 复位
	CommonNode.result reset ()
	// 同步发送Someip Call 不需要修改数据结构，但是需要修改逻辑，在 client 端的 someipPackage 中添加 channel 的信息
	someipResponseContext someipCallSync (1: someipCallContext req)
	// 获取 Someip 协议栈状态 修改入参
	CommonNode.result getSomeipStackStatus (1: CommonNode.netInfo req)
	// 获取所有 SomeipStack Status 的状态 新增函数，需要实现
	someipStackConfig getAllSomeipStackConfig (1: CommonNode.empty req)
	// 获取当前网段存在的服务 修改入参
	someipServiceInfos getAllOfferService (1: CommonNode.netInfo req)
	// 获取当前服务状态列表 修改入参
	serviceStates getServiceStates (1: CommonNode.netInfo req)
	// 启动数据录制 修改入参
	CommonNode.result startLog (1: logRequest req)
	// 停止数据录制 修改入参
	CommonNode.result stopLog (1: logRequest req)
	// 获取当前数据记录任务的状态 修改入参
	CommonNode.result getLogStatus (1: logRequest req)
	// 转换 SomeipDB 文件到 Json
	CommonNode.result convertSomeipDbToJson (1: convertInput req)
	// 转换 SomeipDB 文件到 Py
	CommonNode.result convertSomeipDbToPy (1: convertInput req)
	// 一键设置一个通道的 SomeipConfig
	CommonNode.result setAllSomeipStackConfig (1: someipStackConfig req)
	//Someip message发送相关函数
	CommonNode.result someipPublish(1: someipPackage req)
	CommonNode.result someipSetDefaultAnswer(1: someipPackage req)
	CommonNode.result someipCallAsync(1: someipPackage req)
}
struct someipPackage {
	/**
	   string
	   	SomeIp服务名字
	*/
    1: string serviceName
	/**
	   string
	   	SomeIp报文源IP
	*/
    2: string srcIp
	/**
	   int32
	   	SomeIp报文源端口
	*/
    3: i32 srcPort
	/**
	   string
	   	SomeIp报文目标IP
	*/
    4: string destIp
	/**
	   int32
	   	SomeIp报文目标端口
	*/
    5: i32 destPort
	/**
	   string
	   	SomeIp报文接口类型，支持method
	*/
    6: string interfaceType
    7: i32 serviceId
    8: i32 instanceId
    9: i32 interfaceId
    10: string interfaceName
    11: string context
    12: binary payload
    13: i32 msgType
    14: i32 retCode
    15: i32 sessionId
    16: i32 channel
    17: i64 time
    18: i64 deltaTime
	19: string by
}
struct someipInfo {
	1: CommonNode.result result
	2: string jsonStrInfo
}
struct serviceTag {
	/**
	   string 
	   	服务的名字
	*/
	1: string serviceName
	/**
	   int32 
	   	服务的instance Id
	*/
	2: i32 instanceId
	/**
	   string 
	   	可以是 'consumer'|'provider' 表示该服务设置为什么类型
	*/
	3: string serviceType
	/**
	   bool 
	   	默认值是True，用户可以不用填，如果需要停止服务，该参数赋值False
	*/
	4: bool serviceState = 1
	/**
	   int32 
	   	该服务的通道
	*/
	5: i32 channel = 1
	/**
	   int32 
	   	调用的途径，1:脚本调用|2:GUI调用
	*/
	6: i32 useType = 1
	/**
	   int32 
	   	服务的ID
	*/
	7: i32 serviceId
}
struct someipCallContext {
	2: i32 timeout
	1: someipPackage strContext
	3: i32 channel
}
struct someipResponseContext {
	1: CommonNode.result result
	2: someipPackage strContext
}
struct someipServiceInfo {
	/**
	   string
	   	SomeIp服务名字
	*/
	1: string serviceName
	/**
	   int64
	   	SomeIp服务ID
	*/
	2: i64 serviceId
	/**
	   int32
	   	SomeIp服务InstanceID
	*/
	3: i32 instanceId
	/**
	   string
	   	SomeIp服务源IP地址
	*/
	4: string srcIp
}
struct someipServiceInfos {
	/**
	   result类
	   	请求返回结果
	*/
	1: CommonNode.result result
	/**
	   list[someipServiceInfo]
	   	返回所有服务信息，具体信息查看someipServiceInfo类
	*/
	2: list<someipServiceInfo> infos
}
struct someipArxmlJson {
	/**
	   int32 
	   	执行结果状态值,0是成功，非0失败
	*/
	1: i32 result
	/**
	   string 
	   	执行失败原因描述
	*/
	2: string reason
	/**
	   string 
	   	执行成功后arxml json数据，该值需要使用json.loads转化成字典
	*/
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
	1: CommonNode.result result
	2: list<serviceState> serviceStates
}
// + type
struct someipChannelConfig {
	1: CommonNode.netInfo netInfo
	2: list<string> arxmlPaths
	3: CommonNode.eTHDEVICE ethDevice
}
struct someipStackConfig {
	1: CommonNode.result result
	2: list<someipChannelConfig> configs
	3: list<CommonNode.arpPair> arpPairs
}
struct logRequest {
	1: CommonNode.netInfo netInfo
	2: CommonNode.folderFilePath path
}
struct addSomeipArxmlRequest {
	1: CommonNode.filePath filePath
	2: i32 channel
}

