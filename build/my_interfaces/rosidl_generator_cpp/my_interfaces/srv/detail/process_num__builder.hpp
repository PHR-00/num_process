// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from my_interfaces:srv/ProcessNum.idl
// generated code does not contain a copyright notice

#ifndef MY_INTERFACES__SRV__DETAIL__PROCESS_NUM__BUILDER_HPP_
#define MY_INTERFACES__SRV__DETAIL__PROCESS_NUM__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "my_interfaces/srv/detail/process_num__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace my_interfaces
{

namespace srv
{

namespace builder
{

class Init_ProcessNum_Request_num
{
public:
  Init_ProcessNum_Request_num()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::my_interfaces::srv::ProcessNum_Request num(::my_interfaces::srv::ProcessNum_Request::_num_type arg)
  {
    msg_.num = std::move(arg);
    return std::move(msg_);
  }

private:
  ::my_interfaces::srv::ProcessNum_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::my_interfaces::srv::ProcessNum_Request>()
{
  return my_interfaces::srv::builder::Init_ProcessNum_Request_num();
}

}  // namespace my_interfaces


namespace my_interfaces
{

namespace srv
{

namespace builder
{

class Init_ProcessNum_Response_processed_num
{
public:
  Init_ProcessNum_Response_processed_num()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::my_interfaces::srv::ProcessNum_Response processed_num(::my_interfaces::srv::ProcessNum_Response::_processed_num_type arg)
  {
    msg_.processed_num = std::move(arg);
    return std::move(msg_);
  }

private:
  ::my_interfaces::srv::ProcessNum_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::my_interfaces::srv::ProcessNum_Response>()
{
  return my_interfaces::srv::builder::Init_ProcessNum_Response_processed_num();
}

}  // namespace my_interfaces

#endif  // MY_INTERFACES__SRV__DETAIL__PROCESS_NUM__BUILDER_HPP_
