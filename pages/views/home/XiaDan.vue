<template>
<view class="order">
	
	<!-- 选择配送方式 -->
	<view class="mode" :key="showkey">
	  <text class="text1">Planting Area (square kilometers)</text>
	 <!-- <text class="text2">{{modes || "请选择配送方式"}}</text>
	  <image src="/static/images/home/right.png"></image> -->
	  <view class="right_btn">
	  	<view class="sub" @tap="onsub()">-</view>
	  	<view class="input">
	  		<input :value="S_number" maxlength="2" disabled></input>
	  	</view>
	  	<view class="add" @tap="onadd()">+</view>
	  </view>
	</view>
	<!-- <view class="numbers">
		<text class="price" v-if="item.selectSku">
			￥{{(Number(item.selectSku.money) * item.number).toFixed(2)}}
		</text>
		<text class="price" v-else>
			￥{{(Number(item.money) * item.number).toFixed(2)}}
		</text>
		<view class="right_btn">
			<view class="sub" @tap="onsub(item,index)" :style="'color:' + (item.num == 1?'#ccc':'')">-</view>
			<view class="input">
				<input :value="item.number" maxlength="2" disabled></input>
			</view>
			<view class="add" @tap="onadd(item,index)">+</view>
		</view>
	</view> -->
	
	<view class="morelist">
	  <text class="title">Required materials</text>
	<!--  <view class="right_title">
	    ￥{{sumprice}}
	  </view> -->
	</view>
	
  <!-- 商品详情 -->
  <view v-for="(item, index) in goodsList2" :key="index" class="goods">
    <view class="goods_data">
	  <image :src="item.img" mode="widthFix"></image>
	  <!-- <image mode="widthFix"></image> -->
      <!-- <image :src="item.img" mode="widthFix" ></image> -->
      <view class="goods_title">
        <view class="g_name">{{item.name}}</view>
        <view class="goods_sku"><text style="margin-right: 10upx;">{{item.size}}</text></view>
        <view class="price">
            <view class="t1" :style="'color:' + colors">￥{{Number(item.price_new).toFixed(2)}}</view>
            <view class="t2"><text>￥{{item.price_old.toFixed(2)}}</text></view>
            <view class="t3">x{{item.number}}</view>
          </view>
      </view>
    </view>
	
<!-- 	<view class="morelist" style="border-bottom:none">
	  <view class="title">
	    <text class="quan" :style="'background:' + colors">券</text>
	     <text>优惠券</text>
	  </view>
	  <view class="right_title" :style="'color:' + colors + ';font-size:24upx'" @tap="openCoupon2()">
	    {{item.couponName || '请选择优惠券'}}
	  </view>
	</view> -->	
  </view>
  
  <!-- 订单详情 -->
  <view class="order_more">	  
    <view class="morelist">
      <text class="title">Total price</text>
      <view class="right_title">
        ￥{{this.sum_price_old.toFixed(2)}}
      </view>
    </view>
    <view class="morelist">
      <view class="title">
        <text class="quan" :style="'background:' + colors">lv3</text>
         <text>level</text>
      </view>
      <view class="right_title">
        7% off
      </view>
    </view>
    <view class="morelist">
      <text class="title">Actual payment</text>
      <view class="right_title" :style="'color:' + colors + ';'">
        ￥{{this.sum_price_new.toFixed(2)}}
      </view>
    </view>
	
	<view class="morelist">
	 <!-- <view>
		<text class="title">选择贷款...</text>
		<u-icon name="question-circle" color="grey" size="16" @tap="openCoupon2()"></u-icon>
	  </view> -->
	  <text class="title" @tap="openCoupon2()">Select Loan</text>
	  <!-- <text class="title">?</text> -->
	  <u-icon name="question-circle" color="grey" size="14" @tap="openCoupon2()" style="display: flex;"></u-icon>
	  
	  <view class="right_title" style="vertical-align:middle; display:flex; align-items:center; margin-left: auto;">
	    <u-switch size="22" v-model="checked" @change="handleChange"></u-switch>
	  </view>
	</view>
<!-- 	<view class="morelist" style="border-bottom:0;">
		<u-collapse class="right_title" style="width:100%">
			<u-collapse-item title="贷款政策" ref="collapse" :value="collapse">
				{{this.sum_price_new.toFixed(2)}}
			</u-collapse-item>
		</u-collapse>
	</view> -->
	
<!-- 	<u-collapse>
		<u-collapse-item :title="选择贷款">
			{{item.body}}
		</u-collapse-item>
	</u-collapse> -->
	
  </view>
  
  	</br></br>
  
  <view class="bottom_btn">
    <view class="moneys">
		Total: <text :style="'color:' + colors + ';'">￥{{this.sum_price_new.toFixed(2)}}</text>
    </view>
<!-- 	<view class="btns" :style="'background:' + colors + ';'" @tap="openCoupon2()">
		贷款
	</view> -->
    <view v-if="payway==1" class="btns" :style="'background:' + colors + ';'" @tap="submit">
		Direct Payment
    </view>
	<view v-if="payway==2" class="btns" :style="'background:' + colors + ';'" @tap="submit2">
		Loan Payment
	</view>
  </view>
  <!-- 优惠券弹出层 -->
  <view class="mask" catchtouchmove="preventTouchMove" v-if="couponshow == true" @tap="hidecoupon"></view>
  <view class="coupon" :style="'bottom:' + (couponshow == true ? '0':'')">
    <!-- <view class="buyong" @click="notUsed()">取消贷款</view> -->
    <view class="buyong" @click="notUsed()">X</view>
    <scroll-view class="scrolls" scroll-y>
		<view class="cart_box">
			<text style="font-size:28upx; color:#333; font-weight: bold; text-overflow:ellipsis;">碳账户等级：lv3</text></br>
			<text style="font-size:28upx; color:#333; font-weight: bold; text-overflow:ellipsis;">可贷款额度：6000.00元</text>
			</br></br>
			<view style="width:100%; border:0.5px solid grey"></view>
			</br>
			<text style="font-size:24upx; color:grey; font-weight: bold; text-overflow:ellipsis;">贷款政策</text></br>
			<text style="font-size:24upx; color:grey; text-overflow:ellipsis;">碳账户等级：lv1，可贷款额度：2000.00元，贷款年利率：5.65%</text></br>
			<text style="font-size:24upx; color:grey; text-overflow:ellipsis;">碳账户等级：lv2，可贷款额度：4000.00元，贷款年利率：5.50%</text></br>
			<text style="font-size:24upx; color:grey; text-overflow:ellipsis;">碳账户等级：lv3，可贷款额度：6000.00元，贷款年利率：5.35%</text></br>
			<text style="font-size:24upx; color:grey; text-overflow:ellipsis;">碳账户等级：lv4，可贷款额度：8000.00元，贷款年利率：5.20%</text></br>
			<text style="font-size:24upx; color:grey; text-overflow:ellipsis;">碳账户等级：lv5，可贷款额度：1000.00元，贷款年利率：5.05%</text></br>
			<text style="font-size:24upx; color:grey; text-overflow:ellipsis;">碳账户等级：lv6，可贷款额度：12000.00元，贷款年利率：4.90%</text></br>
			<text style="font-size:24upx; color:grey; text-overflow:ellipsis;">碳账户等级：lv7，可贷款额度：15000.00元，贷款年利率：4.75%</text></br>
		</view>
    </scroll-view>	
	<!-- <view class="new_btns" :style="'background:' + colors + ';'" @tap="submit">贷款并支付</view> -->
  </view>
</view>
</template>

<script>
var app = getApp();
import coupon from "../../commponent/public/coupon";
import {getGoodsData,getAddress,removeAddress} from '@/utils/auth.js'
export default {
  data() {
    return {
		payway: 1,
	  checked: false,
      colors: '',
      couponshow: false,
      modes: '',
	  tapIndex: 99,
	  goodsList:getGoodsData(),
	  couponIndex: 0,
	  nowprice: 0, //临时存储总金额的变量 用于计算优惠券
	  sumprice: 0,
	  address:{
		  name:'反转',
		  phone: 12345678915,
		  address_name:'北京市海淀区苏家坨乡前沙涧村15号'
	  },
	  couponList: [ //优惠券列表
	  	{
	  		money: 30,
	  		reduce: 5,
	  		date: '2020-02-09 2020-10-02',
	  		id: 1,
	  		status: 0,
	  		condition: ['新人专享', '仅在支付时使用', '可与其他产品共享']
	  	}, {
	  		money: 30,
	  		reduce: 5,
	  		date: '2020-02-09 2020-10-02',
	  		id: 2,
	  		status: 0,
	  		condition: ['新人专享']
	  	}
	  ],
	  
	  S_number: 1,
	  sum_price_old: 6897.5,
	  sum_price_new: 6414.675,
	  goods_price: {
		seed: 135,
		fertilizer: 262.5,
		machineSet: 6500,
	  },
	  goodsList2:[
		{
			img: "/static/imagesibm/seed.jpg",
			name: "Selected seeds with high cleanliness and germination rate",
			size: "specification：15kg",
			price_old: 135,
			price_new: 125.55,  //135*0.93
			number: 1
		},
		{
			img: "/static/imagesibm/ferlitizer.jpg",
			name: "Compound fertilizer Stanley brand, contains universal NPK nutrients",
			size: "specification：50kg",
			price_old: 262.5,
			price_new: 244.13,  //262.5*0.93
			number: 1
		},
		{
			img: "/static/imagesibm/machineSet.jpg",
			name: "Tools for sowing, watering, and harvesting",
			size: "specification：1 set",
			price_old: 6500,
			price_new: 6045,  //2500*0.93
			number: 1
		}
	  ],
	  showkey: 0
	  
    };
  },

  components: {
    coupon
  },
  props: {},

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
	removeAddress() //清空存储的地址
	// 计算所有的商品总价
	this.getSumPrice()
    this.setData({
      colors: app.globalData.newColor
    });
  },

  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady: function () {},

  /**
   * 生命周期函数--监听页面显示
   */
  onShow: function () {
	  let address = getAddress() //判断是否存在重新选择的地址
	  if(address && address.name){
		  this.address = address
	  }
  },

  /**
   * 生命周期函数--监听页面隐藏
   */
  onHide: function () {
	  
  },

  /**
   * 生命周期函数--监听页面卸载
   */
  onUnload: function () {},

  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh: function () {},

  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom: function () {},

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage: function () {},
  methods: {
	reSet(){
		this.goodsList2[0].number = this.S_number
		this.goodsList2[1].number = this.S_number
		this.goodsList2[0].price_old = this.goods_price.seed * this.S_number
		this.goodsList2[0].price_new = this.goods_price.seed *0.93 * this.S_number
		this.goodsList2[1].price_old = this.goods_price.fertilizer * this.S_number
		this.goodsList2[1].price_new = this.goods_price.fertilizer *0.93 * this.S_number
		this.sum_price_old = this.goodsList2[0].price_old + this.goodsList2[1].price_old + this.goods_price.machineSet
		this.sum_price_new = this.sum_price_old * 0.93
	},
	onsub() {
		//减少 //已失效商品不做操作
		// if (S_number == 1) {
		// 	return
		// }
		if(this.S_number>1){
			let number = this.S_number
			this.S_number = number - 1
			// this.getSumprice() //计算总价
			this.reSet()
			this.reShow()
		}		
	},	
	onadd() {
		//增加
		let number = this.S_number
		this.S_number = number + 1;
		// this.getSumprice() //计算总价
		this.reSet()
		this.reShow()
	},
	reShow(){
		this.showkey += 1
	},
	  
	  
	getSumPrice(){
		let sumprice = 0
		this.goodsList.forEach(e=>{
			sumprice = (sumprice+Number(e.money)).toFixed(2)
		})
		this.sumprice = sumprice
		this.nowprice = sumprice 
	},
    openCoupon(index) {
      this.setData({
        couponshow: true,
		couponIndex: index
      });
    },
	openCoupon2() {
	  this.setData({
	    couponshow: true,
		// couponIndex: index
	  });
	},
    hidecoupon() {
      this.setData({
        couponshow: false
      });
    },

    submit() {
      //提交订单
      uni.navigateTo({
        url: '/pages/views/order/success?sumprice=' + this.sum_price_new.toFixed(2) 
      });
    },
	submit2() {
	  //提交订单
	  uni.navigateTo({
	    url: '/pages/views/order/successd?sumprice=' + this.sum_price_new.toFixed(2)
	  });
	},
    handleChange(value) {
		if(this.payway==1){
			this.payway = 2;
		}else{
			this.payway = 1;
		}
      // 在开关状态发生变化时触发该函数
      console.log('当前开关状态：', value)
      // 在此处编写需要执行的函数
    },
    selectMode() {
      let that = this;
	  let list = ['物流寄送', '到店自提']
      uni.showActionSheet({
        itemList: list,
        success: function (res) {
			that.setData({
			  modes: list[res.tapIndex],
			  tapIndex: res.tapIndex
			});
        }
      });
    },
	
    setAddress() {
      uni.navigateTo({
        url: '/pages/views/user/myaddress'
      });
    },
	onReceive(item, index){ //选择优惠券
		this.couponshow = false
		/**
		 * 自定义变量 到goodsList中 用户计算合计金额与优惠券
		 */
		this.goodsList[this.couponIndex].couponName = '满'+item.money+'减'+item.reduce
		this.goodsList[this.couponIndex].couponReduce = item.reduce //优惠券金额
		this.sumprice = this.sumprice - item.reduce
	},
	notUsed(){ //不使用优惠券 重置金额
		
		this.couponshow = false
		this.goodsList[this.couponIndex].couponName = ''
		if(this.goodsList[this.couponIndex].couponReduce){
			this.sumprice = this.sumprice + Number(this.goodsList[this.couponIndex].couponReduce)
		}
	}
  }
};
</script>
<style lang="scss" scoped>
page {
  background-color: #FFFFFF;
}

.order {
  padding: 20upx 4%;
}
.mode{
  height: 80upx;
  line-height: 80upx;
  display: flex;
  justify-content: space-between;
  background-color: #fff;
  padding: 0 20upx;
  border-radius: 10upx;
  align-items: center;
  margin-bottom: 20upx;
  box-shadow: 0upx 0upx 10upx #ddd;
}
.mode:active{
  background-color: #f5f5f5;
}
.mode .text1{
  color: #999;
  font-size: 24upx;
}
.mode .text2{
  font-size: 24upx;
  color: #333;
  display: block;
  width: 50%;
  font-weight: bold;
}
.mode image{
  width: 40upx;
  height: 40upx;
  display: block;
}
.order_address {
  height: 150upx;
  width: 100%;
  background-color: #fff;
  border-radius: 10upx;
  overflow: hidden;
  position: relative;
  box-shadow: 0upx 0upx 10upx #ddd;
}

.order_address image {
  width: 100%;
  height: 100%;
  display: block;
  position: absolute;
  top: 0;
  left: 0;
  z-index: 10;
}

.address_box {
  width: 100%;
  height: 100%;
  display: block;
  position: absolute;
  top: 0;
  left: 0;
  z-index: 10;
  box-sizing: border-box;
  padding: 20upx;
  display: flex;
  align-items: center;
}

.weizhi_icon text {
  font-size: 40upx;
  margin-left: 10upx;
}

.address_box .center {
  margin-left: 20upx;
}

.address_box .center .name {
  height: 60upx;
  line-height: 60upx;
}

.address_box .center .name .text1 {
  font-size: 26upx;
  font-weight: bold;
  color: #333;
  display: inline-block;
  margin-right: 20upx;
}

.phones {
  font-size: 24upx;
  color: #999;
  z-index: 0;
}

.address_box .address_name {
  font-size: 26upx;
  font-weight: bold;
  color: #333;
}

.noaddress {
  margin-left: 40upx;
  font-weight: bold;
  color: #333;
  font-size: 26upx;
}

.goods {
  background-color: #fff;
  margin-top: 20upx;
  box-shadow: 0upx 0upx 10upx #ddd;
  border-radius: 10upx;
  padding: 20upx;
  padding-bottom: 10upx;
}

.goods_data {
  width: 100%;
  display: flex;
  margin-bottom: 15upx;
}

.goods_data image {
  min-width: 150upx;
  max-width: 150upx;
  height: 150upx;
  display: block;
  border-radius: 10upx;
}

.goods_title {
  margin-left: 20upx;
  line-height: 40upx;
  width: 100%;
}
.goods_title .price{
  width: 100%;
  display: flex;
  height: 40upx;
  line-height: 40upx;
  margin-top: 20upx;
  position: relative;
}
.goods_title .price .t1{
  font-size: 30upx;
  font-weight: bold;
  display: block;
}
.goods_title .price .t2{
  font-size: 24upx;
  margin-left: 15upx;
  display: block;
  color: #999;
  text-decoration: line-through;
}
.goods_title .price .t3{
  float: right;
  font-weight: bold;
  font-size: 28upx;
  color: #999;
  position: absolute;
  right: 0upx;
  top: 0;
}
.goods_title .g_name {
  font-size: 26upx;
  font-weight: bold;
  max-height: 80upx;
  overflow: hidden;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
}
.goods_title .goods_sku{
  color: #999;
  /* margin-top: 20upx; */
}
.numbers{
  /* text-align: right; */
}
.shop{
  margin-top: 20upx;
  font-size: 24upx;
  color: #333;
  display: flex;
  align-content: center;
}
.shop .iconfont{
  margin-right: 20upx;
}
.order_more{
  padding: 0 2%;
  margin-top: 20upx;
}
.morelist{
  height: 80upx;
  line-height: 80upx;
  display: flex;
  justify-content: space-between;
  // border-bottom: 1upx dashed #eee;
}
.morelist .title{
  color: #333;
  font-size: 26upx;
  font-weight: bold;
  display: flex;
  align-items: center;
}
.morelist .title .quan{
  font-size: 20upx;
  width: 35upx;
  height: 35upx;
  line-height: 36upx;
  text-align: center;
  border-radius: 8upx;
  margin-right: 10upx;
  align-items: center;
  color: #fff;
}
.morelist .right_title{
  color: #999;
}
.tips{
  padding: 10upx 0;
  margin-bottom: 120upx;
}
.tips .tips_name{
  font-size: 26upx;
  font-weight: bold;
  line-height: 60upx;
}
.textarea_box{
  min-height: 100upx;
  width: 100%;
  border: 1upx solid #eee;
  border-radius: 10upx;
  padding: 20upx;
}
.textarea_box textarea{
  font-size: 24upx;
  height: 150upx;
}
.bottom_btn{
  height: 100upx;
  width: 100vw;
  background-color: #fff;
  position: fixed;
  left: 0;
  bottom: 0;
  line-height: 100upx;
  display: flex;
  justify-content: flex-end;
  padding: 0 30upx;
  z-index: 100;
  font-weight: bold;
}
.bottom_btn .moneys{
  font-size: 28upx;
  font-weight: bold;
  margin-right: 100upx;
}
.bottom_btn .btns{
  font-size: 28upx;
  color: #fff;
  height: 60upx;
  line-height: 60upx;
  padding: 0 25upx;
  text-align: center;
  border-radius: 40upx;
  margin-top: 20upx;
  font-weight: bold;
}
.new_btns{
	// height: 100upx;
	// width: 100vw;
	// background-color: #fff;
	// position: fixed;
	// left: 0;
	// bottom: 0;
	line-height: 60upx;
	// display: flex;
	// justify-content: flex-end;
	// padding: 0 30upx;
	// z-index: 100;
	// font-weight: bold;
	
	// font-size: 28upx;
	color: #fff;
	height: 60upx;
	// line-height: 60upx;
	// padding: 0 25upx;
	text-align: center;
	border-radius: 40upx;
	// margin-top: 20upx;
	font-weight: bold;
}
.cart_box {
	margin-top: 20upx;
	padding-bottom: 100upx;
}
.cart_list {
		width: 92vw;
		height: calc(22vw + 34upx);
		border-radius: 12upx;
		box-shadow: 0px 4upx 16upx rgba(0, 0, 0, .1);
		z-index: 4;
		overflow: hidden;
		border: 0;
		display: flex;
		align-items: center;
		position: relative;
		margin-bottom: 20upx;
	}
/* 优惠券 */
.coupon{
  background-color: #fff;
  border-radius: 10upx 10upx 0 0;
  position: fixed;
  left: 0;
  bottom: -1000upx;
  z-index: 150;
  transition: all 0.3s;
}
.coupon .buyong{
  line-height: 80upx;
  padding: 0 4%;
  text-align: right;
  color: #999;
}
.mask{
  width: 100%;
  height: 100%;
  position: fixed;
  top: 0;
  left: 0;
  background: #000;
  z-index: 10;
  opacity: 0.7;
}
.scrolls{
  width: 100vw;
  height: 55vh;
  z-index: 500;
}

.mode{
  height: 80upx;
  line-height: 80upx;
  display: flex;
  justify-content: space-between;
  background-color: #fff;
  padding: 0 20upx;
  border-radius: 10upx;
  align-items: center;
  margin-bottom: 20upx;
  box-shadow: 0upx 0upx 10upx #ddd;
}
.mode:active{
  background-color: #f5f5f5;
}
.mode .text1{
  color: #999;
  font-size: 24upx;
}
.mode .text2{
  font-size: 24upx;
  color: #333;
  display: block;
  width: 50%;
  font-weight: bold;
}
.right_btn {
		display: flex;
		justify-content: center;
		align-items: flex-end;
		margin-right: 20rpx;
	}

	.right_btn .sub {
		width: 40rpx;
		height: 40rpx;
		font-size: 40rpx;
		background-color: #f3f3f3;
		border-radius: 4rpx;
		text-align: center;
		line-height: 40rpx;
	}

	.right_btn .sub:active {
		background-color: #f8f8f8;
	}

	.right_btn .input {
		width: 50rpx;
		height: 50rpx;
		margin: 0 8rpx;
		background-color: #f3f3f3;
	}

	.right_btn .input input {
		width: 50rpx;
		height: 50rpx;
		display: flex;
		font-size: 22rpx;
		text-align: center;
		align-items: center;
		justify-content: center;
		color: $mycolor;
	}

	.right_btn .add {
		width: 40rpx;
		height: 40rpx;
		font-size: 40rpx;
		background-color: #f3f3f3;
		border-radius: 4rpx;
		text-align: center;
		line-height: 40rpx;
	}

	.right_btn .add:active {
		background-color: #f8f8f8;
	}
</style>