include "Common.thrift"

service canUdsNode {
	Common.result subscribe (1: node_info req)
	kvlist generate_key (1: request_para req)
	Common.result diag_request(1: can_diag_message req)
	Common.result diag_response(1: can_diag_message req)
}

struct can_diag_message {
  1: i32 id
  2: list<i16> cmd
  3: i8 dlc
  4: bool is_fd
}

struct node_info {
  1: i32 request_id_phys
  2: i32 response_id
  3: i32 request_id_func
  4: i32 channel
}

struct request_para {
  1: list<i32> seed_value
  2: i32 algorithm_number
}

struct kvlist {
  1: list<i32> key_value
}