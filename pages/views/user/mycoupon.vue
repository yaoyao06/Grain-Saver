<template>
		<view class="cart_box">
			<text style="font-size:28upx; color:#333; font-weight: bold; text-overflow:ellipsis;">碳账户等级：lv3</text></br>
			<text style="font-size:28upx; color:#333; font-weight: bold; text-overflow:ellipsis;">可贷款额度：6000.00元，贷款年利率：5.35%</text>
			</br></br>
			<view style="width:100%; border:0.5px solid grey"></view>
			</br>
			<text style="font-size:24upx; color:grey; font-weight: bold; text-overflow:ellipsis;">等级权限</text></br>
			<text style="font-size:24upx; color:grey; text-overflow:ellipsis;">碳账户等级：lv1\n购买优惠：无，可贷款额度：2000.00元，贷款年利率：5.65%</text></br>
			<text style="font-size:24upx; color:grey; text-overflow:ellipsis;">碳账户等级：lv2\n购买优惠：96折，可贷款额度：4000.00元，贷款年利率：5.50%</text></br>
			<text style="font-size:24upx; color:grey; text-overflow:ellipsis;">碳账户等级：lv3\n购买优惠：93折，可贷款额度：6000.00元，贷款年利率：5.35%</text></br>
			<text style="font-size:24upx; color:grey; text-overflow:ellipsis;">碳账户等级：lv4\n购买优惠：91折，可贷款额度：8000.00元，贷款年利率：5.20%</text></br>
			<text style="font-size:24upx; color:grey; text-overflow:ellipsis;">碳账户等级：lv5\n购买优惠：89折，可贷款额度：1000.00元，贷款年利率：5.05%</text></br>
			<text style="font-size:24upx; color:grey; text-overflow:ellipsis;">碳账户等级：lv6\n购买优惠：87折，可贷款额度：12000.00元，贷款年利率：4.90%</text></br>
			<text style="font-size:24upx; color:grey; text-overflow:ellipsis;">碳账户等级：lv7\n购买优惠：85折，可贷款额度：15000.00元，贷款年利率：4.75%</text></br>
		</view>
</template>

<script>
var app = getApp();
import loading from "../../commponent/public/loading";

export default {
  data() {
    return {
      colors: '',
      couponList: [{
        name: '满100减10',
        dates: '2020-02-09 2020-03-02',
        status: 0,
        money: 100,
        sub: 10
      }, {
        name: '满100减10',
        dates: '2020-02-09 2020-03-02',
        status: 1,
        money: 100,
        sub: 10
      }],
      isShow: true
    };
  },

  components: {
    loading
  },
  props: {},

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    this.setData({
      colors: app.globalData.newColor
    });
    setTimeout(() => {
      this.setData({
        isShow: false
      });
    }, 600);
  },

  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady: function () {},

  /**
   * 生命周期函数--监听页面显示
   */
  onShow: function () {},

  /**
   * 生命周期函数--监听页面隐藏
   */
  onHide: function () {},

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
	  jumpNext(){
		  uni.showToast({
		  	title:'根据需求进行跳转~',
			icon:'none'
		  })
	  }
  }
};
</script>
<style lang="scss" scoped>
.coupon_box{
  margin: 20upx;
  box-shadow: 0upx 0upx 10upx #ddd;
  position: relative;
  border-radius: 10upx;
  overflow: hidden;
}
.coupon_box .left{
  width: 70%;
  display: flex;
  align-items: center;
  flex-wrap: wrap;
  padding: 20upx;
  float: left;
}
.coupon_box .left .hui{
  width: 40upx;
  height: 40upx;
  font-size: 20upx;
  color: #fff;
  background-color: #EC1818;
  border-radius: 8upx;
  line-height: 40upx;
  text-align: center;
  display: inline-block;
  transform: translateY(-5upx);
}
.coupon_box .left .left_top{
  width: 60vw;
  display: block;
  font-size: 26upx;
  font-weight: bold;
  
}
.left_top .hui_name{
  line-height: 60upx;
  height: 60upx;
  margin-left: 20upx;
  display: inline-block; 
}
.left_bottom{
  font-size: 24upx;
  font-weight: bold;
  color: #333;
  height: 60upx;
  line-height: 60upx;
}
.coupon_box .right{
  text-align: center;
  height: 160upx;
  width: 180upx;
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  align-content: center;
  background-color: #A8A8A8;
  float: right;
}
.coupon_box .right .shiyong{
  height: 40upx;
  line-height: 40upx;
  background-color: #fff;
  border-radius: 20upx;
  padding: 0 20upx;
  color: #A8A8A8;
}
.coupon_box .right .money{
  font-size: 45upx;
  color: #fff;
}
.coupon_box .right text{
  font-size: 24upx;
  color: #fff;
  height: 40upx;
  line-height: 34upx;
}
.coupon_box .bottom{
  height: 60upx;
  line-height: 60upx;
  display: flex;
  align-content: flex-start;
  font-size: 24upx;
  margin-top: 10upx;
}
.coupon_box .bottom view{
  margin-right: 20upx;
  color: #888;
  font-weight: bold;
}
.ysy{
  width: 80upx;
  height: 80upx;
  position: absolute;
  top: 20upx;
  right: 200upx;
}
</style>