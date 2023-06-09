<template>
	<!-- 我的足迹 -->
	<view>
		<view class="mycollection">
			<view class="cart_box">
				<view v-for="(item, index) in dataList" :key="index" class="cart_list">
					<!-- 左边：作物图片 -->
					<view class="cover" @tap="jumpDetails(item,index)" >
						<image :src="item.img" mode="aspectFill"></image>
					</view>
					<!-- 右边：方案信息 -->
					<view class="right">
						<!-- 作物名称 -->
						<view class="goods_name" @tap="jumpDetails(item,index)">
							{{item.name}}
						</view>						
						<view class="numbers">
							<text class="price">
								 return：￥{{item.money}}/km²
							</text>
							<text class="browse">
								emissions：{{item.carbon}}/km²
							</text>
						</view>												
					</view>					
				</view>
			</view>
		</view>
		<loading v-if="isShow == true"></loading>
	</view>
</template>

<script>
	var app = getApp();
	import loading from "../../commponent/public/loading";
	import navBar from '../../commponent/public/navBar.vue'
	export default {
		data() {
			return {
				colors: '',
				dataList: [
					{
						name: 'Wheat',
						img: "/static/imagesibm/wheat.png",
						money: '2000~3000',
						carbon: '130kg'
						// carbon: '0.75千克碳当量'
					}, {
						name: 'Rice',
						img: "/static/imagesibm/rice.jpg",
						money: '3000~5000',
						carbon: '230kg'
					}, {
						name: 'Corn',
						img: "/static/imagesibm/corn.jpg",
						money: '1500~2000',
						carbon: '200kg'
					}
					// , {
					// 	name: '棉花 棉花 棉花 棉花 棉花 棉花 棉花 棉花 棉花 棉花',
					// 	img: "/static/imagesibm/cotton.jpeg",
					// 	money: '35.90',
					// 	carbon: '5.90'
					// },
				],
				isShow: true
			};
		},

		components: {
			loading,
			navBar
		},
		props: {},

		/**
		 * 生命周期函数--监听页面加载
		 */
		onLoad: function(options) {
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
		onReady: function() {},

		/**
		 * 生命周期函数--监听页面显示
		 */
		onShow: function() {},

		/**
		 * 生命周期函数--监听页面隐藏
		 */
		onHide: function() {},

		/**
		 * 生命周期函数--监听页面卸载
		 */
		onUnload: function() {},

		/**
		 * 页面相关事件处理函数--监听用户下拉动作
		 */
		onPullDownRefresh: function() {},

		/**
		 * 页面上拉触底事件的处理函数
		 */
		onReachBottom: function() {},

		/**
		 * 用户点击右上角分享
		 */
		onShareAppMessage: function() {},
		methods: {
			jumpDetails(item,index) {
				//跳转详情
				uni.navigateTo({
					url: '/pages/views/home/XiaDan'
				});
			},
		}
	};
</script>
<style scoped lang="scss">
	.mycollection {
		padding: 10upx 4%;
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

	.cart_list .checkbox-box {
		padding-left: 16upx;
		flex-shrink: 0;
		height: 22vw;
		margin-right: 16upx;
		align-items: center;
		position: relative;
		width: 50upx;
	}

	.cart_list .checkbox-box .checkbox {
		width: 28upx;
		height: 28upx;
		border-radius: 100%;
		border: solid 1upx;
		position: absolute;
		top: 50%;
		left: 20upx;
		display: flex;
		align-items: center;
		justify-content: center;
		transform: translateY(-50%);
	}

	.cart_list .checkbox-box .checkbox .on {
		width: 20upx;
		height: 20upx;
		border-radius: 100%;
		align-items: center;
	}

	.cart_list .cover {
		width: 22vw;
		height: 22vw;
		flex-shrink: 0;
		margin-left: 10upx;
		border-radius: 8upx;
		overflow: hidden;
		margin-right: 20upx;
	}

	.cart_list .cover image {
		width: 100%;
		height: 100%;
		display: block;
	}

	.daodi {
		text-align: center;
		font-size: 24upx;
		color: #ccc;
		margin-top: 30upx;
	}

	.right {
		height: 22vw;
		width: 100%;
		/* overflow: hidden; */
		display: flex;
		flex-wrap: wrap;
		padding-right: 15upx;
		position: relative;
	}

	.right .goods_name {
		width: 100%;
		font-size: 24upx;
		line-height: 60upx;
		max-height: 68upx;
		color: #333;
		overflow: hidden;
		font-weight: bold;
		text-overflow: ellipsis;
		display: -webkit-box;
		-webkit-line-clamp: 2;
		-webkit-box-orient: vertical;
	}

	.sku {
		font-size: 22upx;
		height: 50upx;
		line-height: 50upx;
		color: #a7a7a7;
		margin-bottom: 40upx;
	}

	.numbers {
		position: absolute;
		width: 100%;
		overflow: hidden;
		display: flex;
		justify-content: space-between;
		align-items: center;
		height: 70upx;
		bottom: -5upx;
		.browse{
			font-size: 20upx;
			color: #999;
			margin-right: 20upx;
		}
	}

	.numbers .price {
		font-size: 20upx;
		line-height: 50upx;
		color: $mycolor;
	}

	.numbers .right_btn {
		display: flex;
		justify-content: center;
		align-items: flex-end;
		margin-right: 20upx;
	}

	.right_btn .sub {
		width: 40upx;
		height: 40upx;
		font-size: 40upx;
		background-color: #f3f3f3;
		border-radius: 4upx;
		text-align: center;
		line-height: 40upx;
	}

	.right_btn .sub:active {
		background-color: #f8f8f8;
	}

	.right_btn .input {
		width: 50upx;
		height: 50upx;
		margin: 0 8upx;
		background-color: #f3f3f3;
	}

	.right_btn .input input {
		width: 50upx;
		height: 50upx;
		display: flex;
		font-size: 22upx;
		text-align: center;
		align-items: center;
		justify-content: center;
	}

	.right_btn .add {
		width: 40upx;
		height: 40upx;
		font-size: 40upx;
		background-color: #f3f3f3;
		border-radius: 4upx;
		text-align: center;
		line-height: 40upx;
	}

	.right_btn .add:active {
		background-color: #f8f8f8;
	}

	.del_mask {
		width: 100%;
		height: 100%;
		position: fixed;
		top: 0;
		left: 0;
		z-index: -21;
	}

	.dask_del {
		width: 100%;
		height: 100%;
		position: absolute;
		top: 0;
		left: 0;
		background-color: rgba(0, 0, 0, .5);
		z-index: -20;
		display: flex;
		align-items: center;
		opacity: 0;
		transition: all 0.3s;
	}

	.dask_del .del,
	.cencal {
		width: 100upx;
		height: 100upx;
		display: flex;
		justify-content: center;
		line-height: 100upx;
		border-radius: 100%;
		text-align: center;
		font-size: 24upx;
		background: linear-gradient(#FF5D39, #FFAF48);
		color: #ffffff;
		font-weight: 500;
		margin: 0 auto;
	}

	.dask_del text:active {
		opacity: 0.9;
	}

	.cencal {
		background: linear-gradient(#FFE846, #FFCD43);
	}
</style>
