// Version = 1.0.20220131


/**
 *
 *以太网设备的类型，后面不断在这里追加
 *
 */
enum eTHDEVICE {
	eTHDEVICEPC = 0 // 本机电脑
	eTHDEVICEVECTOR = 1 // Vector 以太网硬件
}
// 执行结果
struct result {
	// result: 0 -> 正常
	// result: 0 - 999 -> 自定义返回码
	// result: 1000 -> 有异常
	1: i32 result
	2: string reason
}
// 空
struct empty {
}
// 版本信息
struct version {
	1: string version
	2: string releaseDate
}
struct arpPair {
	1: list<i32> ipAddress
	2: list<i32> macAddress
}
// 网络信息 mac mask port switch igmp arp[]
struct netInfo {
	1: string ipAddr
	2: string iface
	3: i32 status
	4: i32 channel
	5: list<i32> macAddress
	6: list<i32> mask
	7: string virtualPort
	8: string switch
	9: string ethernetName
	10: list<i32> igmpAddress
	11: list<i32> gateway
	13: i32 vlan
	14: list<arpPair> arpPairs
}
// 文件地址
struct filePath {
	1: string path
}
// 文件夹和文件名地址
struct folderFilePath {
	1: string folder
	2: string file
}
// 通用字符串 >>>>>>
struct genericString {
	1: result result
	2: string text
}
struct genericInt {
	1: i32 index
}
struct genericInt64 {
	1: i64 index
}
struct linChannelInfo {
	1: i32 softwareChannel
	2: string hardwareChannel
	3: string databaseChannel // 数据库路径
	4: i32 isMaster = 0
	5: i32 bitrate = 0
	6: i32 deviceId = 0x0
    7: i64 combaudrate = 19200
    8: i32 major_version = 2
    9: i32 minor_version = 1
    10: i32 txreceipts = 1
    11: list<byte> DLC = [] //paser不需要要，stack需要，此DLC对应id dlc信息，如{1：8,2:6}
	12: i16 hardwareType =  0
	13: string appname
	14: list<byte> initData = [] //paser不需要要，stack需要，此初始值对应id初始值字典，如{1：[0,1,2,3]}
	15: list<i8> id = [] //paser不需要要，stack需要，此id是真实需要用到的ID
	16: list<i8> time = [] //paser不需要要，stack需要，此time是对应id的调度表时间,因为时间事float类型需要json dump

}

struct linChannelConfigs{
	1: list<linChannelInfo> linChannelConfigs
}
