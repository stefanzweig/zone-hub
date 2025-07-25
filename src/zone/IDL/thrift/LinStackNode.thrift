include "CommonNode.thrift"


service linStackNode {
	// 复位 LinStackNode
	CommonNode.result reset ()
	// 设置 LinStack 的配置
	CommonNode.result setConfig (1: CommonNode.genericString req)
	CommonNode.result setChannelConig(1:CommonNode.linChannelConfigs req)
	// 启动 LinStack
	CommonNode.result startLinStack ()
	// 关闭 LinStack
	CommonNode.result stopLinStack ()
	CommonNode.result setMessageSimulation (1: linMessageConfig req)
	CommonNode.result setHeaderSimulation (1: linHeaderConfig req)
	CommonNode.result setMessageData (1: linMessageDataT req)
	// 获取 LinStack 的状态
	linStackStatus getStatus ()
	CommonNode.result clearSubscribe ()
	CommonNode.result clearSend (1: CommonNode.genericInt req)
	CommonNode.result setLinCrcConfig (1: linCrcConfig req)
	CommonNode.result clearLinCrcConfig (1: linCrcConfig req)
	CommonNode.genericInt64 getDeltaTime()
}
struct linMessageConfig {
	/**
	   int32
	   	LIN报文ID
	*/
	1: i32 id
	/**
	   bool
	   	LIN报文是否仿真
	*/
	2: bool simu
	/**
	   int32
	   	LIN报文所在的软件通道
	*/
	3: i32 channel
}
struct linHeaderConfig {
	/**
	   int32
	   	LIN节点所在的软件通道
	*/
	2: i32 channel
	/**
	   bool
	   	LIN调度表是否需要仿真，此功能只适用于主节点模式
	*/
	1: bool simu
}
struct linMessageDataT {
	/**
	   int32
	   	LIN报文所在的软件通道
	*/
	1: i32 channel
	/**
	   int32
	   	LIN报文ID
	*/
	2: i32 id
	/**
	   list[int32]
	   	LIN报文源数据
	*/
	3: list<i32> data
}

struct linStackStatus {
	/**
	   result
	   	调用结果返回值，为result类
	*/
	1: CommonNode.result result 
	/**
	   int32
	   	比如 0->正在运行; 1->未运行; 2->没有硬件;等等
	*/
	2: i32 status
	/**
	   string
	   	预留，显示字符串提示信息
	*/
	3: string strStatus
}
struct linCrcConfig {
	/**
	   int32
	   	需要设置CRC报文所在软件通道
	*/
	1: i32 channel
	/**
	   int32
	   	需要设置CRC报文ID
	*/
	2: i32 id
	/**
	   int32
	   	需要设置CRC所在起始位
	*/
	3: i32 crcBitStart
	/**
	   int32
	   	需要设置RC所在起始位
	*/
	4: i32 rcBitStart
	/**
	   int32
	   	需要设置CRC信号所占的位长度
	*/
	5: i32 crcBitLen
	/**
	   int32
	   	需要设置RC信号所占的位长度
	*/
	6: i32 rcBitLen
	/**
	   int32
	   	需要设置RC最小值
	*/
	7: i32 rcMinValue
	/**
	   int32
	   	需要设置RC最大值
	*/
	8: i32 rcMaxValue
	/**
	   list[int32]
	   	CRC table
	*/
	9: list<i32> crcTable
	/**
	   int32
	   	RC步长设置
	*/
	10: i32 stepLen
}


