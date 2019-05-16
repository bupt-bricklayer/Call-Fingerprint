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
## 社会网络构图初步  
依据上述数据，考虑构建其社会网络的数据形式。我们依据opp_operator字段提取出与其同运营商的部分数据，并与全数据集比较，若存在cus_num与其opp_num号码相同的则为第一类数据，与其不同的或运营商不同的数据为第二类，故可以依据第一类数据来构图，再依据第二类数据来部分完善该图的节点属性。在完善节点和边属性的部分，依据原始数据里的字段，call_type、start_time、call_dur、roam_code、roam_type、longdis_type均可归为边属性，而cus_num、lac、cellid、attr_code则作为节点属性，opp_num、opp_attr_num作为对端节点属性，再通过另外一条对应数据完善其lac和cellid，这样便可以构建出一个运营商内部的社会网络，便可利用社会网络的方法分析问题。  
根据上面的方法，可以得出初步的原始运营商内部的电信社会网络，虽然对于大数据集来说其网络的组建信息仍十分有限，但该方法由于其社会网络特性可以作为一个切入方向。  
如下为网络中的一条路径：  
****
![](https://github.com/bupt-bricklayer/Call-Fingerprint/raw/master/picture/网络路径.png)  
****
可以看出该图中节点属性为四维向量，边属性为七维向量，这对于存储来说是非常不利的，无论是采用edgelist形式还是邻接矩阵形式都需要采用其它文件和标签来记录节点和边的属性向量，还需要通过记录第二类数据来完善该节点属性信息，其数据处理复杂度和处理完成后的数据集大小都是巨大的，故这里可采用一些降维的方法来缩减数据量，并通过结果来变更降维方法，以达到更优化的特征提取的目的。  
# 手工特征提取方法的探究  
我们尝试了不同的手工特征提取的方法，包括从多元的非网络数据和社会网络节点特征提取方向，并利用距离算法来初步比对了各种不同方法的优劣，虽然使用距离算法并不能完全展现出特征提取的优劣，只能展示它们的线性分类的好坏，但可以初步判别一些异常较为明显的提取方法。我们的工作目前仅限于在多元的非网络数据方向提出了特征提取的一套方案，社会网络节点特征方向的比对仍需继续研究。  
## 非网络方向目前的提取方法  
为了达到效果，我们在研究了不同的通信数据理论的基础上，在整理了数据之后，对比分析了原始数据中各条的差异度后得出了一些结论。例如：  
****
![](https://github.com/bupt-bricklayer/Call-Fingerprint/raw/master/picture/漫游区号和对端号码归属区号归一化后对比图.png)  
图三 漫游区号和对端号码归属区号归一化后对比图
****
由图可以看出漫游地区号和对端号码归属区号的异常率（即不在本区的次数占总次数的比例）分布起伏较大，不同客户的位置移动频率是不同的，有很大差别。但大多数用户的位置信息异常率为0，因此异常率对于异常率不为0的用户识别贡献度很高，但对异常率为0的用户识别贡献率为0。  
****
![](https://github.com/bupt-bricklayer/Call-Fingerprint/raw/master/picture/不同用户通话次数趋势图.png)  
图四 不同用户通话次数趋势图
****
由于不同用户的工作需要和交通圈大小不同，其月通话次数也会有很大不同。从其分布图来看，不同用户的通话次数分布变化很大，对识别不同的用户贡献度较高。  
****
![](https://github.com/bupt-bricklayer/Call-Fingerprint/raw/master/picture/用户通话时间分布对比.png)  
图五 用户通话时间分布对比
****
用户每次通话时间以30s为间隔分类，用来反映用户每次通话时间趋势。由上图可看出：在选取的用户中，通话时间基本控制在60s以内，其中绝大部分在30s以内，这可以作为用户的通话特征。  
具体的对比结果将展示在项目主页中。我们通过这些结论，初步总结了以下原则：  
- 通话类型：有其固定的类型不予以处理；
- 对端号码以及位置信息：由于对端号码和位置信息由唯一码编码加密，本项目取其频率最高的几位建立起交往圈。其中选取频率最高的五个对端号码以及频率最高的三个lac以及ceilid号码并去其后四位。
- 通话时长：分为十个维度区分不同的通话时长。
- 通话开始时间：全天分为四个时段、全月分为上中下旬进行统计。
- 漫游地区号和对端号码归属区号：由于用户通话位置的确定性，这两个属性少有变动，只需计算其异常率即可。
