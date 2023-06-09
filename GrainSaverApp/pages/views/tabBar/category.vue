<template>
	<view class="category">
		<!-- 搜索 -->
		<!-- #ifdef APP-PLUS -->
		<div class="status-bar" :style="{height:statusBarHeight+'px'}"></div>
		<!-- #endif -->
		<view class="search">
			<search class="search_box"></search>
		</view>
		<!-- 二级类型的分类菜单 -->
		<!-- hideShow 显示销量与价格筛选条件 -->
		<twostage :colors="colors" :showHeader="showHeader" :bottoms="bottoms" :current="currentTwo" :dataList="dataList" :classList="categoryList" v-if="classLevel == true"
		 :hideShow="true" @setTwo="setTwo"></twostage>
	</view>
</template>

<script>
	var app = getApp();
	import search from "../../commponent/public/search";
	import twostage from "../../commponent/cate/twostage";
	import threestage from "../../commponent/cate/threestage";

	export default {
		data() {
			return {
				bottoms: '100',
				showHeader: false, //判断当前终端是APP还是h5
				classLevel: true, //控制显示分类菜单  true：二级分类菜单   false：三级分类菜单
				colors: "",
				current: "",
				scrollTop: "",
				statusBarHeight: 20,
				categoryList: [{ //分类列表
					id: 1,
					name: 'Rice',

				}, {
					id: 2,
					name: 'Wheat',

				}, {
					id: 3,
					name: 'Corn',

				}
				],
				// 二级菜单目录
				dataList: [{
						title: 'Westsea Agro-products Processing Company',
						type: 1,
						goods_id: 201,
						money: '1.58',
						number: 1,
						hmoney: '45.90',
						img: '/static/imagesibm/shuidao1.jpg',
						distance: '35.8',
						tan: '8.234',
						youhui: false,
						baoyou: false,
						status: 0, //商品过期状态  0正常  1已失效
						stock: 600,
						sku: [],
						skuArr: [
						]
					},
					{
						title: 'Fukang Agricultural Wholesale Market',
						type: 1,
						goods_id: 202,
						money: '1.57',
						number: 75,
						hmoney: '39.90',
						distance: '13.5',
						tan: '3.105',
						img: '/static/imagesibm/shuidao2.jpg',
						youhui: false,
						baoyou: false,
						status: 0, //商品过期状态  0正常  1已失效
						stock: 100,
						sku: [],
						skuArr: [
						]

					},
					{
						title: 'Binhu Agricultural Processing Company',
						type: 1,
						goods_id: 203,
						money: '1.58',
						number: 1,
						hmoney: '162.00',
						distance: '76.3',
						tan: '17.549',
						img: '/static/imagesibm/shuidao3.jpeg',
						youhui: false,
						baoyou: false,
						status: 0, //商品过期状态  0正常  1已失效
						stock: 200,
						sku: [],
						skuArr: []
					},
					{
						title: 'Westsea Agro-products Processing Company',
						type: 2,
						goods_id: 204,
						money: '2.1',
						number: 1,
						hmoney: '99.00 ',
						youhui: false,
						baoyou: false,
						distance: '35.8',
						tan: '8.234',
						stock: 100,
						img: '/static/imagesibm/xiaomai1.jpeg',
						status: 0, //商品过期状态  0正常  1已失效
						sku: [ ],
						skuArr: [
						]
					},
					{
						title: 'Fukang Agricultural Wholesale Market',
						type: 2,
						goods_id: 205,
						money: '2.2',
						number: 1,
						hmoney: 35.00,
						distance: '13.5',
						tan: '3.105',
						img: '/static/imagesibm/xiaomai2.jpeg',
						youhui: false,
						baoyou: false,
						stock: 500,
						status: 0, //商品过期状态  0正常  1已失效
						skuArr: [
						],
						sku: [
						]
					},
					{
						title: 'Binhu Agricultural Processing Company',
						type: 2,
						goods_id: 206,
						money: '2.1',
						number: 200,
						hmoney: '70.90',
						youhui: false,
						baoyou: false,
						distance: '76.3',
						tan: '17.549',
						img: '/static/imagesibm/xiaomai3.jpeg',
						status: 0, //商品过期状态  0正常  1已失效
						stock: 140,
						sku: [ ],
						skuArr: [],
					},
					{
							title: 'Westsea Agro-products Processing Company',
							type: 3,
							goods_id: 201,
							money: '3.5',
							number: 1,
							distance: '35.8',
							tan: '8.234',
							hmoney: '45.90',
							img: '/static/imagesibm/yumi1.jpg',
							youhui: false,
							baoyou: false,
							status: 0, //商品过期状态  0正常  1已失效
							stock: 600,
							sku: [],
							skuArr: []
						},
						{
							title: 'Fukang Agricultural Wholesale Market',
							type: 3,
							goods_id: 202,
							money: '3.6',
							number: 75,
							hmoney: '39.90',
							distance: '13.5',
							tan: '3.105',
							img: '/static/imagesibm/yumi2.jpg',
							youhui: false,
							baoyou: false,
							status: 0, //商品过期状态  0正常  1已失效
							stock: 100,
							sku: [],
							skuArr: [
							]
					
						},
						{
							title: 'Binhu Agricultural Processing Company',
							type: 3,
							goods_id: 203,
							money: '3.5 ',
							number: 1,
							hmoney: '162.00',
							distance: '76.3',
							tan: '17.549',
							img: '/static/imagesibm/yumi3.jpg',
							youhui: false,
							baoyou: false,
							status: 0, //商品过期状态  0正常  1已失效
							stock: 200,
							sku: [],
							skuArr: []
						}
				],
				currentTwo: 0,
				currentThere: 0
			};
		},

		components: {
			search,
			twostage,
			threestage
		},
		props: {},

		/**
		 * 生命周期函数--监听页面加载
		 */
		onLoad: function(options) {
			// #ifdef APP-PLUS
			this.showHeader = true   //在APP端对样式进行调整
			this.bottoms = '0'  //在APP下 规格弹窗的位置发生变化
			// #endif
		},

		/**
		 * 生命周期函数--监听页面初次渲染完成
		 */
		onReady: function() {},

		/**
		 * 生命周期函数--监听页面显示
		 */
		onShow: function() {
			this.setData({
				colors: app.globalData.newColor
			});
		},

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
			setCurrent(e) {
				//设置tab
				let index = e.currentTarget.dataset.index;
				let items = e.currentTarget.dataset.item;
				let scrollTop = index * 20;

				if (index <= 2) {
					scrollTop = 0;
				}

				this.setData({
					current: index,
					scrollTop: scrollTop
				});
			},
			onswitch() {
				this.setData({
					classLevel: !this.classLevel
				});
			},
			setThere(item) { //获取选择的三级tab
				console.log(item)
			},
			setTwo(item) { //获取选择的二级tab
				console.log(item)
			}
		}
	};
</script>
<style scoped lang="scss">
	.category {
		background-color: #ffffff;
		position: fixed;
		width: 100%;
		height: 100%;
		box-sizing: border-box;
		top: 0;
		bottom: 0;
		z-index: 10;
	}
	.search {
		padding: 10upx 1% 10upx;
		padding-left: 10upx;
		overflow: hidden;
		display: flex;
		align-items: center;
		justify-content: space-between;
	}

	.search_box {
		width: 100%;
	}

	.hierarchy {
		width: 10%;
		height: 60upx;
		font-size: 32upx;
		text-align: right;
	}
</style>
