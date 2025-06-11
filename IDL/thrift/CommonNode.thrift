// Version = 1.0.20220131


/**
 *
 *以太网设备的类型，后面不断在这里追加
 *eTHDEVICEPC 本机电脑
 *eTHDEVICEVECTOR vector网卡
 */
enum eTHDEVICE {
	/**
	   本机电脑
	 */
	eTHDEVICEPC = 0 
	/**
	   Vector 以太网硬件
	 */
	eTHDEVICEVECTOR = 1
}

/**
 *
 *执行结果
 *
 */
struct result {
	/**
	   int32 
	   	执行结果状态值
	*/
	1: i32 result
	/**
	   string 
	   	执行结果原因
	*/
	2: string reason
}

// 空
struct empty {
}

/**
 *
 *版本
 *
 */
struct version {
	/**
	   string 
	   	版本信息
	*/
	1: string version
	/**
	   string 
	   	版本释放日期
	*/
	2: string releaseDate
}

/**
 *
 *arp信息表
 *
 */
struct arpPair {
	/**
	   list[int32] 
	   	ip地址信息
	*/
	1: list<i32> ipAddress
	/**
	   list[int32] 
	   	mac地址信息
	*/
	2: list<i32> macAddress
}

/**
 *
 *网卡信息
 *
 */
struct netInfo {
	/**
	   string
	   	网卡IP地址信息，例如'172.31.3.2'
	*/
	1: string ipAddr
	/**
	   string
	   	网卡名字，例如'以太网 1'
	*/
	2: string iface
	/**
	   int32
	   	网卡状态值
	*/
	3: i32 status
	/**
	   int32
	   	网卡设置通道
	*/
	4: i32 channel
	/**
	   list[int32]
	   	mac地址信息，目前vector网卡需要设置，本机网卡无需设置，只需要在电脑本机以太网配置即可
	*/
	5: list<i32> macAddress 
	/**
	   list[int32]
	   	子网掩码信息，目前vector网卡需要设置，本机网卡无需设置，只需要在电脑本机以太网配置即可
	*/
	6: list<i32> mask
	/**
	   string
	   	虚拟port名字，目前vector网卡需要设置，本机网卡无需设置
	*/
	7: string virtualPort
	/**
	   string
	   	vector网卡所在switch名字，目前vector网卡需要设置，本机网卡无需设置
	*/
	8: string switch
	/**
	   string
	   	vector网卡所在Ethernet名字，目前vector网卡需要设置，本机网卡无需设置
	*/
	9: string ethernetName
	/**
	   list[int32]
	   	网卡IGMP信息，目前vector网卡需要设置，本机网卡无需设置
	*/
	10: list<i32> igmpAddress
	/**
	   list[int32]
	   	网卡网关信息，目前vector网卡需要设置，本机网卡无需设置
	*/
	11: list<i32> gateway
	/**
	   int32
	   	网卡VLAN信息，目前vector网卡需要设置，本机网卡无需设置
	*/
	13: i32 vlan
	/**
	   list[arpPair]
	   	网卡arp信息，目前vector网卡需要设置，本机网卡无需设置
	*/
	14: list<arpPair> arpPairs
}

/**
 *
 *文件地址，也可以当作普通字符串使用
 *
 */
struct filePath {
	/**
	   string
	   	文件地址信息，普通字符串
	*/
	1: string path
}

/**
 *
 *文件夹和文件名地址
 *
 */
struct folderFilePath {
	/**
	   string
	   	文件夹信息，普通字符串
	*/
	1: string folder
	/**
	   string
	   	文件地址信息，普通字符串
	*/
	2: string file
}


/**
 *
 *字符串加result结构组合
 *
 */
struct genericString {
	/**
	   result
	   	执行结果得数据结构，引用本文件中result
	*/
	1: result result
	/**
	   string
	   	普通字符串，传递需要的信息
	*/
	2: string text
}

/**
 *
 *普通32位整型
 *
 */
struct genericInt {
	/**
	   int32
	   	普通整型，传递需的信息
	*/
	1: i32 index
}

/**
 *
 *普通64位整型
 *
 */
struct genericInt64 {
	/**
	   int64
	   	普通整型，传递需的信息
	*/
	1: i64 index
}

/**
 *
 *LIN 通道信息
 *
 */
struct linChannelInfo {
	/**
	   int32
	   	LIN 软件通道信息，软件通道用户自己定义，此通道用于报文通道定义，包括trace报文中通道信息
	*/
	1: i32 softwareChannel
	/**
	   string
	   	LIN 硬件通道信息，硬件通道信息为读取到的硬件信息，如vector 'VN1640 123434 1',1640+序列号+通道
	*/
	2: string hardwareChannel
	/**
	   string
	   	LIN 加载数据库路径，需要绝对路径
	*/
	3: string databaseChannel
	/**
	   int32
	   	LIN 通道模式，是否作为主节点模式，1表示主节点模式，0表示从节点模式
	*/
	4: i32 isMaster = 0
	/**
	   int32
	   	LIN 通道波特率，一般设置192000
	*/
	5: i32 bitrate = 0
	/**
	   int32
	   	vector设备不用设置，该参数用于USB_LIN PC识别COM的index
	*/
	6: i32 deviceId = 0x0
	/**
	   int64
	   	该参数用于USB_LIN 与 PC 间通信波特率设置
	*/
    7: i64 combaudrate = 19200
	/**
	   int32
	   	LIN 主版本信息
	*/
    8: i32 major_version = 2
	/**
	   int32
	   	LIN 小版本信息
	*/
    9: i32 minor_version = 1
	/**
	   int32
	   	LIN 是否接收自身发送的报文，1表示接收，0表示不接收
	*/
    10: i32 txreceipts = 1
	/**
	   list[int8]
	   	LIN 所有报文（ID：1-64）DLC信息，LIN解析节点设置不需要设置，LIN发送节点需要设置，如不设置全部按照DLC=8
	*/
    11: list<i8> DLC = []
	/**
	   int16
	   	LIN 硬件类型，可以查看枚举ZSDEVICE信息
	*/
	12: i16 hardwareType =  0
	/**
	   string
	   	vector设备需要设置
	*/
	13: string appname
	/**
	   list[int8]
	   	LIN 所有报文初始值信息，此初始值对应id初始值字典，如{1：[0,1,2,3]}，然后将该字典转化bytes后转成list[int8]
	*/
	14: list<i8> initData = [] //paser不需要要，stack需要，此初始值对应id初始值字典，如{1：[0,1,2,3]}
	/**
	   list[int8]
	   	调度表中对应ID列表，顺序也需要和调度表一致，LIN解析节点设置时不需要，发送节点需要设置
	*/
	15: list<i8> id = [] 
	/**
	   list[int8]
	   	调度表中对应ID后的时间，顺序也需要和调度表一致，LIN解析节点设置时不需要，发送节点需要设置
	   	此time是对应id的调度表时间,因为时间事float类型需要将该列表转化成bytes,然后转成list进行发送
	*/
	16: list<i8> time = []

}

struct linChannelConfigs{
	/**
	   list[linChannelInfo]
	   	多条LIN配置，list中元素为本文件中linChannelInfo
	*/
	1: list<linChannelInfo> linChannelConfigs
}

/**
 *
 *ZoneMaster支持硬件类型，后面不断在这里追加
 *VECTOR  vector设备
 *PEAK 包括PCAN,PLIN目前不支持
 *USBDEVICE 目前支持USB_LIN
 *FIRE2 英特佩斯硬件
 */
enum ZSDEVICE {
	VECTOR = 0 
	PEAK = 2
	BMMUST = 4
	USBDEVICE = 8
	FIRE2 = 16
}
