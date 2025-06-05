include "Common.thrift"


service linStackNode {
	// 复位 LinStackNode
	Common.result reset ()
	// 设置 LinStack 的配置
	Common.result setConfig (1: Common.genericString req)
	Common.result setChannelConig(1:Common.linChannelConfigs req)
	// 启动 LinStack
	Common.result startLinStack ()
	// 关闭 LinStack
	Common.result stopLinStack ()
	Common.result setMessageSimulation (1: linMessageConfig req)
	Common.result setHeaderSimulation (1: linHeaderConfig req)
	Common.result setMessageData (1: linMessageDataT req)
	// 获取 LinStack 的状态
	linStackStatus getStatus ()
	Common.result clearSubscribe ()
	Common.result clearSend (1: Common.genericInt req)
	Common.result setLinCrcConfig (1: linCrcConfig req)
	Common.result clearLinCrcConfig (1: linCrcConfig req)
	Common.genericInt64 getDeltaTime()
}
struct linMessageConfig {
	1: i32 id
	2: bool simu
	3: i32 channel
}
struct linHeaderConfig {
	2: i32 channel
	1: bool simu
}
struct linMessageDataT {
	1: i32 channel
	2: i32 id
	3: list<i32> data
}
struct linStackConfig {
	// Lin Stack 的配置数据结构
	// TODO 邢潇 根据实际情况完善
	1: string hardwareType
	2: string appName
}
struct linStackConfigs {
	// Lin Stack Config 列表。用列表表达多路 Lin 的配置
	1: list<linStackConfig> config
}
struct linStackStatus {
	// Lin Stack 的状态信息
	// TODO 邢潇 根据实际情况修改
	1: Common.result result // 返回结果
	2: i32 status // 比如 0->正在运行; 1->未运行; 2->没有硬件;等等
	3: string strStatus
}
struct linCrcConfig {
	1: i32 channel
	2: i32 id
	3: i32 crcBitStart
	4: i32 rcBitStart
	5: i32 crcBitLen
	6: i32 rcBitLen
	7: i32 rcMinValue
	8: i32 rcMaxValue
	9: list<i32> crcTable
	10: i32 stepLen
}


