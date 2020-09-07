



### 全自动pipeline设想：
全自动Pipeline： 
maya相机路径导出fbx 

-> 上传shotgun 

-> 通知Build machine：下载相关fbx资源然后import 到unreal的sequencer camera track 

-> 上传shotgun +push 新资源到版本控制 

-> 通知渲染machine：同步最新版本 自动渲染shot 上传渲染结果 

-> 合成


# 技术细节

# Shotgun事件处理可以采取两种，
### 第一种方式：
用Shotgun的事件触发器框架：

https://github.com/shotgunsoftware/shotgunevents/wiki

通过在插件注册回调函数进行事件处理，这里有样例代码：

https://github.com/shotgunsoftware/shotgunEvents/wiki/API#registerCallbacks

### 第二种方式：

用Shotgun的webhook来访问

https://developer.shotgunsoftware.com/zh_CN/3d448f5e/

第一种方式实现比较方便直接用python就可以完成了，第二种方式来说更加灵活一些，因为不一定非要使用python并且编写插件，完全可以直接让shotgun去访问一个另外的服务器或者是在服务器上托管的应用
