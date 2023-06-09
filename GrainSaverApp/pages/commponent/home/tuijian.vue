<template>
<view class="hots" @tap="jumptest">
    <view class="left_icon">
      <text class="iconfont icon-huangguan" :style="'color:' + colors"></text>
    </view>
    <view class="center">
      <view class="p1">Crop Recommendations</view>
      <!-- <view class="p2">New Products Listed</view> -->
    </view>
    <view class="right">
      <image src="/static/images/home/right.png" class="right_img"></image>
    </view>
</view>
</template>

<script>

export default {
  data() {
    return {};
  },

  components: {},
  props: {
    colors: {
      type: String
    }
  },
  methods: {
	  jumptest(e) {
	  
	  console.log('dlasjhd')
	      uni.navigateTo({
	          url: '/pages/views/home/Tuijian'
	      });
	  
	  }
  },
  
};
</script>
<style lang="scss" scoped>
.hots{
  margin: 0 3%;
  margin-top: 20upx;
  height: 110upx;
  border-bottom: 1upx solid #F8F8F8;
  overflow: hidden;
}
.hots:active{
  opacity: 0.8;
}
.left_icon{
  float: left;
}
.left_icon .iconfont{
  font-size: 46upx;
  display: inline-block;
  margin-right: 20upx;
  line-height: 100upx;
}
.center{
  float: left;
}
.p1{
  font-size: 34upx;
  font-weight: 500;
  color: #000;
  line-height: 70px;
  // margin-top: 10upx;
}
.p2{
  font-size: 24upx;
  color: #999;
}
.right{
  float: right;
}
.right .right_img{
  width: 40upx;
  height: 40upx;
  display: inline-block;
  margin-top: 28upx;
}
</style>