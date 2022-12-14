// Generated by gencpp from file etasb_msgs/point2DArray.msg
// DO NOT EDIT!


#ifndef ETASB_MSGS_MESSAGE_POINT2DARRAY_H
#define ETASB_MSGS_MESSAGE_POINT2DARRAY_H


#include <string>
#include <vector>
#include <memory>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <std_msgs/Header.h>

namespace etasb_msgs
{
template <class ContainerAllocator>
struct point2DArray_
{
  typedef point2DArray_<ContainerAllocator> Type;

  point2DArray_()
    : header()
    , x()
    , y()  {
    }
  point2DArray_(const ContainerAllocator& _alloc)
    : header(_alloc)
    , x(_alloc)
    , y(_alloc)  {
  (void)_alloc;
    }



   typedef  ::std_msgs::Header_<ContainerAllocator>  _header_type;
  _header_type header;

   typedef std::vector<double, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<double>> _x_type;
  _x_type x;

   typedef std::vector<double, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<double>> _y_type;
  _y_type y;





  typedef boost::shared_ptr< ::etasb_msgs::point2DArray_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::etasb_msgs::point2DArray_<ContainerAllocator> const> ConstPtr;

}; // struct point2DArray_

typedef ::etasb_msgs::point2DArray_<std::allocator<void> > point2DArray;

typedef boost::shared_ptr< ::etasb_msgs::point2DArray > point2DArrayPtr;
typedef boost::shared_ptr< ::etasb_msgs::point2DArray const> point2DArrayConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::etasb_msgs::point2DArray_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::etasb_msgs::point2DArray_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::etasb_msgs::point2DArray_<ContainerAllocator1> & lhs, const ::etasb_msgs::point2DArray_<ContainerAllocator2> & rhs)
{
  return lhs.header == rhs.header &&
    lhs.x == rhs.x &&
    lhs.y == rhs.y;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::etasb_msgs::point2DArray_<ContainerAllocator1> & lhs, const ::etasb_msgs::point2DArray_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace etasb_msgs

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::etasb_msgs::point2DArray_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::etasb_msgs::point2DArray_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::etasb_msgs::point2DArray_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::etasb_msgs::point2DArray_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::etasb_msgs::point2DArray_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::etasb_msgs::point2DArray_<ContainerAllocator> const>
  : TrueType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::etasb_msgs::point2DArray_<ContainerAllocator> >
{
  static const char* value()
  {
    return "bb81c9745207cb7bf500b9c5063554f2";
  }

  static const char* value(const ::etasb_msgs::point2DArray_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xbb81c9745207cb7bULL;
  static const uint64_t static_value2 = 0xf500b9c5063554f2ULL;
};

template<class ContainerAllocator>
struct DataType< ::etasb_msgs::point2DArray_<ContainerAllocator> >
{
  static const char* value()
  {
    return "etasb_msgs/point2DArray";
  }

  static const char* value(const ::etasb_msgs::point2DArray_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::etasb_msgs::point2DArray_<ContainerAllocator> >
{
  static const char* value()
  {
    return "# Array for point2D\n"
"\n"
"Header header\n"
"\n"
"float64[] x\n"
"float64[] y\n"
"================================================================================\n"
"MSG: std_msgs/Header\n"
"# Standard metadata for higher-level stamped data types.\n"
"# This is generally used to communicate timestamped data \n"
"# in a particular coordinate frame.\n"
"# \n"
"# sequence ID: consecutively increasing ID \n"
"uint32 seq\n"
"#Two-integer timestamp that is expressed as:\n"
"# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')\n"
"# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')\n"
"# time-handling sugar is provided by the client library\n"
"time stamp\n"
"#Frame this data is associated with\n"
"string frame_id\n"
;
  }

  static const char* value(const ::etasb_msgs::point2DArray_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::etasb_msgs::point2DArray_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.header);
      stream.next(m.x);
      stream.next(m.y);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct point2DArray_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::etasb_msgs::point2DArray_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::etasb_msgs::point2DArray_<ContainerAllocator>& v)
  {
    s << indent << "header: ";
    s << std::endl;
    Printer< ::std_msgs::Header_<ContainerAllocator> >::stream(s, indent + "  ", v.header);
    s << indent << "x[]" << std::endl;
    for (size_t i = 0; i < v.x.size(); ++i)
    {
      s << indent << "  x[" << i << "]: ";
      Printer<double>::stream(s, indent + "  ", v.x[i]);
    }
    s << indent << "y[]" << std::endl;
    for (size_t i = 0; i < v.y.size(); ++i)
    {
      s << indent << "  y[" << i << "]: ";
      Printer<double>::stream(s, indent + "  ", v.y[i]);
    }
  }
};

} // namespace message_operations
} // namespace ros

#endif // ETASB_MSGS_MESSAGE_POINT2DARRAY_H
