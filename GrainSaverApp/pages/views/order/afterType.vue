<template>
	<view class="after_type">
		<view class="goods_data">
			<image :src="goodData.img" mode=""></image>
			<view class="right">
				<p class="goods_name">{{goodData.title}}</p>
				<p class="goods_sku">{{goodData.goods_sku_text}}</p>
				<p class="goods_price">
					<text :style="{color:colors}">￥{{goodData.money}}</text>
					<text style="font-size: 24upx;color: #333333;">数量 x {{goodData.number}}</text>
				</p>
			</view>
		</view>
		<!-- 分割线 -->
		<view class="place"></view>
		<!-- 选择退货类型 -->
		<view class="_type">
			<!-- 退货 -->
			<view class="type_list" @click="jumpNext(1,'退货')">
				<view class="type_left">
					<image class="type_img" src="/static/images/after/tuihuo.png" mode=""></image>
					<text class="type_text">退货</text>
				</view>
				<view class="type_right">
					<view class="left_p">
						<p style="text-align: right;">退回收到的商品</p>
						<p style="color:#E1251B">支持7天无理由退货</p>
						<p style="color:#E1251B">(拆封后不支持)</p>
					</view>
					<image src="/static/images/home/right.png" mode=""></image>
				</view>
			</view>
			<!-- 换货 -->
			<view class="type_list" v-for="(item,index) in lists" :key="index" @click="jumpNext(item.type,item.name)">
				<view class="type_left">
					<image class="type_img" :src="item.icon" mode=""></image>
					<text class="type_text">{{item.name}}</text>
				</view>
				<view class="type_right">
					<view class="left_p">
						<p>{{item.tips}}</p>
					</view>
					<image src="/static/images/home/right.png" mode=""></image>
				</view>
			</view>
			
		</view>
	</view>
</template>

<script>
	var app = getApp();
	export default {
		data() {
			return {
				colors:"",
				goodData: {},
				lists:[
					{name:'换货',type: 2,icon:'/static/images/after/huanhuo.png',tips:'更换收到的商品'},
					{name:'维修',type: 3,icon:'/static/images/after/weixiu.png',tips:'维修收到的商品'},
				]
			}
		},
		onLoad(option) {
			let goodData = JSON.parse(option.goodData)
			this.setData({
				goodData: goodData,
				colors: app.globalData.newColor
			});
		},
		methods:{
			jumpNext(index,typeText){
				uni.setStorageSync('goodData',JSON.stringify(this.goodData)) // 存储商品信息
				uni.navigateTo({
					url: '/pages/views/order/afterSale?type='+index+'&typeText='+typeText
				})
			}
		}
	}
</script>

<style lang="scss" scoped>
	.after_type {
		padding: 20upx 0;
		background-color: #fff;
	}

	.goods_data {
		display: flex;
		align-items: center;
		justify-content: flex-start;
		overflow: hidden;
		padding: 0 4%;
		image {
			width: 140upx;
			height: 140upx;
			border-radius: 8upx;
		}

		.right {
			margin-left: 20upx;
			width: 80%;

			.goods_name {
				font-size: 26upx;
				font-weight: bold;
				overflow: hidden;
				display: -webkit-box;
				-webkit-line-clamp: 2;
				-webkit-box-orient: vertical;
			}

			.goods_sku {
				font-size: 24upx;
				color: #999999;
				margin-top: 5upx;
			}

			.goods_price {
				display: flex;
				align-items: center;
				justify-content: space-between;
				font-size: 28upx;
				color: #999;
				margin-top: 5upx;
			}
		}
	}
	.place{
		height: 20upx;
		width: 100%;
		margin-top: 20upx;
		border-bottom: 2upx dashed #EEEEEE;
	}
	._type{
		margin: 0 4%;
		border-radius: 20upx;
		box-shadow: 0upx 0upx 10upx #DDDDDD;
		margin-top: 30upx;
		box-sizing: border-box;
		padding: 20upx;
		.type_list{
			height: 152upx;
			box-sizing: border-box;
			display: flex;
			align-items: center;
			justify-content: space-between;
			border-bottom: 1upx solid #EEEEEE;
			padding: 20upx 0;
			&:last-of-type{
				border-bottom: none;
			}
			&:active{
				opacity: .8;
			}
			.type_left{
				display: flex;
				align-items: center;
				.type_img{
					width: 50upx;
					height: 50upx;
					display: block;
				}
				.type_text{
					font-size: 30upx;
					font-weight: bold;
					color: #202020;
					margin-left: 20upx;
				}
			}
			.type_right{
				display: flex;
				align-items: center;
				.left_p{
					margin-right: 10upx;
					p{
						height: 30upx;
						line-height: 30upx;
						font-size: 24upx;
						text-align: center;
						color: #999999;
					}
				}
				image{
					width: 40upx;
					height: 40upx;
					display: block;
					float: right;
				}
			}
		}
	}
</style>
