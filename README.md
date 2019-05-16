Call-Fingerprint
===========================
运营商部分电信社会网络数据的最佳呼叫指纹特征提取的研究
****
![](https://github.com/bupt-bricklayer/Call-Fingerprint/raw/master/picture/logo.jpg)
****
# 项目背景  
为了改变当前“数据丰富知识匮乏”的状况，数据挖掘技术得到了众多企业的重视。电信行业竞争激烈，重入网和潮汐用户给运营商带来资源消耗。当前国内外对于使用电信数据建立呼叫指纹库的研究主要集中于重入网侦测和用户离网预警手段研究等方面，通过数据挖掘的算法探求数据和用户特征的关系，并通过历史数据搭建一个呼叫指纹库，再利用现有数据构建用户特征，判别用户的重入网现象和预警用户离网，以实现资源的合理分配。本项目主要着重于利用分类和比对算法研究对电信社会网络数据的特征提取，即对呼叫指纹库的建立，并希望借用数据挖掘算法探究出一套可行的特征提取方案，建立某一特定条件下性能最佳的呼叫指纹库。  
随着大数据概念的普及，数据挖掘算法越来越受到运营商的重视。首先其坐拥大量用户数据，有充足的数据量来对其用户进行行为特征研究，其次，其对于用户特征研究的需求随着用户行为的异常而不断提高，例如本项目的研究方向即服务于用户的重入网识别，许多实际上相同的用户会恶意申请多个号码进行一些特殊操作，以达到获利的目的。在这样的背景下，在一定的用户范围下研究用户特征的提取算法，以达到识别最优化的目的，这一研究变得日益重要。故本项目基于运营商的部分用户社会网络数据，从对数据最基本的理论认识提取特征开始，通过分类和比对算法来对比特征提取的优劣，并逐步深入理解各数据类对结果的贡献度，从而逐渐优化呼叫指纹库的提取方案，提出在一定条件下最优化的电信社会网络数据特征提取算法。  
# 运营商部分社会网络数据类型介绍  
## 原始数据格式  
下面介绍运营商部分电信数据的格式。由于运营商数据难以获得，下面介绍的是部分经过加密后的数据以及数据类型。我们希望通过这一介绍逐步深入建立对这一特殊数据类型的理解,从而初步建立其社会网络模型。如图一所示为该数据的基本数据类型，其中字段call_type即为呼叫类型，其中1代表主叫，2代表被叫；字段cus_num代表本端号码，即发起通话的号码（经过加密的）；字段opp_num代表对端的号码，其可能有本运营商的同时也有其它运营商的（也是经过加密的）；字段start_time代表该通话发起的时间；字段call_dur代表该通话持续的时间（秒）；lac和cellid字段都是用户的位置信息，即位置区识别码和蜂窝小区id；attr_code字段代表本端的归属区号；roam_code字段表示其漫游地的归属区号；opp_attr_code字段表示对端的归属区号；roam_type字段代表漫游类型，属性值可为1至5；opp_operator代表对端运营商，属性值可以为1至3；longdis_type代表长途通话类型，属性值可以为1至5。  
****
![](https://github.com/bupt-bricklayer/Call-Fingerprint/raw/master/picture/数据格式类型.png)  
图一 数据格式类型
****
如图二，原始数据的格式为“一对多”的形式，即一个cus_num对应着多个opp_num，对应每个cus_num分为一个部分的话，每个部分都详细的描述了该cus_num在一定时间范围内的通话信息，包括每一个通话记录的详细信息，由此可见原始数据提供的信息量非常大而且非常具体，不考虑算法可实现性和复杂度的问题时，可直接利用原始数据进行比对，但由于数据挖掘领域研究的不断深入，呼叫指纹的概念被提出，对原始数据进行比对分析，通过手工提取或数学理论算法进行特征提取以建立完备的特征库，该特征库即为呼叫指纹库，提取出的用户特征即称为呼叫指纹，这可以是多元的非网络数据的特征提取问题，也可以是社会网络节点特征提取的问题。  
****
![](https://github.com/bupt-bricklayer/Call-Fingerprint/raw/master/picture/部分数据.png)  
图二 部分数据
****
