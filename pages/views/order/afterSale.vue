<template>
	<view class="cencal_order">
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
		<!-- 退货理由 -->
		<view class="other">
			<view class="remark">
				<textarea maxlength="-1" placeholder="请在此处输入您的退单理由" placeholder-class="textarea_p"></textarea>
			</view>
			<view class="tag_box">
				<view v-for="(item, index) in remarkList" :key="index" class="tag_list" @tap="setCurrent(index)">
					<view :style="'color:' + (item.current == true ?'#fff':'') + ';background:' + (item.current == true ? colors:'') + ';border:' + (item.current == true ? 'none':'')">
						{{item.name}}
					</view>
				</view>
			</view>
			<p class="youhui" style="border-bottom: none;">
				<text class="text1">上传凭证</text>
				<text class="text3">(最多3张)</text>
			</p>
			<view class="img_box">
				<view class="img_list" v-for="(item, index) in imgUrl" :key="index">
					<block v-if="item.type == 1">
						<image :src="item.url" mode="" @click="previewImg(item.url)" class="imgs"></image>
						<image z-index="9999" src="/static/images/search/close.png" mode="" class="close" @tap="delImg(index)"></image>
					</block>
					<block v-if="item.type == 2">
						<video :src="item.url" :poster="item.poster" :controls="false" :show-center-play-btn="false" :show-play-btn="false"
						 :enable-progress-gesture="false">
							<cover-view class="covers"></cover-view>
							<cover-image v-if="showVideo == false" class="imgs" src="/static/images/goods/bofang.png" mode="" @click="onshowVideo(item.url)"></cover-image>
							<cover-image z-index="900" v-if="showVideo == false" src="/static/images/search/close.png" mode="" class="video_close" @tap="delImg(index)"></cover-image>
						</video>
					</block>
				</view>
				<view class="addImg" v-if="imgUrl.length < 3" @tap="onChoose">
					<image src="/static/images/shexiang.png" mode=""></image>
					<p>添加图片/视频</p>
				</view>
			</view>
		</view>
		<!-- 退货的返回方式以及收件地址 -->
		<view class="address">
			<view class="address_type">
				<text class="type_text">返回方式</text>
				<view class="type_right" @click="setReturn">
					<text>{{types}}</text>
					<image src="/static/images/home/dian.png" class="more" mode=""></image>
				</view>
			</view>
			<view class="rule">
				<view class="rule_left">如因个人原因退/换货，将在换新商品签收时收取8元运费</view>
				<view class="rule_right">
					运费规则
				</view>
			</view>
			<block v-if="tapIndex == 0">
				<view class="user_address" @click="setLocation(0)" :style="{borderBottom:tapIndex== 0?'1upx solid #eee':'none'}">
					<view>
						<view class="u_a_top">
							<text class="iconfont icon-dizhi"></text>
							<text class="name">{{Pickaddress.name}}</text>
							<text>{{Pickaddress.phone | formatPhone}}</text>
						</view>
						<view class="u_a_bottom">
							地址: {{Pickaddress.address}}{{Pickaddress.moreAddres}}
						</view>
					</view>
					<image src="/static/images/home/right.png" mode=""></image>
				</view>
				<view class="times" @click="openPopup">
					<image class="rili" src="/static/images/home/riil.png" mode=""></image>
					<view class="times_title">
						{{pickTime}}
					</view>
					<image src="/static/images/home/dian.png" class="more" mode=""></image>
				</view>
			</block>
		</view>
		<!-- 收货地址 只有在换货和维修时才显示 -->
		<view class="address" v-if="type != 1">
			<p class="m_a_title">收货地址<text>(该地址是商家回寄给您的地址)</text></p>
			<view class="user_address" @click="setLocation(1)" style="border-bottom: none;">
				<view>
					<view class="u_a_top">
						<text class="iconfont icon-dizhi"></text>
						<text class="name">{{Toaddress.name}}</text>
						<text>{{Toaddress.phone | formatPhone}}</text>
					</view>
					<view class="u_a_bottom">
						地址: {{Toaddress.address}}{{Toaddress.moreAddres}}
					</view>
				</view>
				<image src="/static/images/home/right.png" mode=""></image>
			</view>
		</view>
		<!-- 联系人信息 -->
		<view class="contacts">
			<view class="user_cell">
				<image src="/static/images/home/cat.png" mode=""></image>
				<text>{{Toaddress.name}}</text>
			</view>
			<view class="user_cell">
				<image src="/static/images/home/phone.png" mode=""></image>
				<text>{{Toaddress.phone | formatPhone}}</text>
			</view>
		</view>
		<p class="tips">
			提交服务单后，售后专员可能与您电话沟通，请保持手机畅通
		</p>
		<view class="btns" :style="{background: colors}" @click="onsubmit">
			确认提交
		</view>
		<!-- 预览视频弹窗APP 小程序 -->
		<view class="mask" v-if="showVideo == true" @touchmove.stop.prevent="ondefault" @click="hideShow">
			<view class="close">
				<image src="/static/images/goods/close.png"></image>
			</view>
		</view>
		<view class="previewvideo" v-if="showVideo == true">
			<view class="videos">
				<video class="nowvideos" id="nowVideo" v-if="showVideo == true" :src="videos" :autoplay="showVideo"
				 :show-center-play-btn="true" :show-mute-btn="true" :show-fullscreen-btn="false"></video>
			</view>
		</view>
		<!-- 用来承载H5预览视频的 -->
		<view style="position: absolute;top: -999upx;left: -999upx;">
			<video ref="newVideo" id="newVideo" :src="videos" :autoplay="showVideo" :show-center-play-btn="false" :show-mute-btn="true"
			 :show-fullscreen-btn="false"></video>
		</view>
		<set-times @onComplete="onComplete" @onClose="onClose" :shows="shows"></set-times>
	</view>
</template>

<script>
	var app = getApp();
	import setTimes from '@/pages/commponent/order/setTime.vue'
	import {
		getPickaddress,
		getToaddress,
		removePickaddress,
		removeToaddress
	} from '@/utils/auth.js'
	export default {
		data() {
			return {
				colors: '',
				type: 1,
				platform:'',
				types: '上门取件',
				tapIndex: 0,
				shows: false,
				showVideo: false,
				videos: '',
				pickTime: '', //取货时间
				remarkList: [{
					name: '个人原因'
				}, {
					name: '性价比太低'
				}, {
					name: '态度不好'
				}, {
					name: '价格不合理'
				}, {
					name: '做工不行'
				}, {
					name: '物流时间长'
				}, {
					name: '价格优惠低'
				}, {
					name: '其他原因'
				}],
				data: "",
				imgUrl: [],
				goodData: {},
				Pickaddress: {
					name: '反转',
					phone: '17712333156',
					address: '安徽省合肥市庐阳区',
					moreAddres: '逍遥津',
					address_id: 1
				},
				Toaddress: {
					name: '反转',
					phone: '17712333156',
					address: '安徽省合肥市庐阳区',
					moreAddres: '逍遥津',
					address_id: 1
				}
			};
		},
		filters: {
			formatPhone(value) {
				var reg = /(\d{3})\d{4}(\d{4})/; //正则表达式
				var phone = value.replace(reg, "$1****$2")
				return phone
			}
		},
		components: {
			setTimes
		},
		props: {},
		created() {
			this.platform = uni.getSystemInfoSync().platform  //判断当前是安卓还是ios 然后进行适配
			this.newVideo = uni.createVideoContext('newVideo');
		},
		/**
		 * 生命周期函数--监听页面加载
		 */
		onLoad: function(options) {
			removePickaddress() //清空选择的取货地址
			removeToaddress() //清空选择的收件地址
			// ↑ 页面加载清空缓存的取货地址和收货地址
			let goodData = JSON.parse(uni.getStorageSync('goodData')) //获取商品信息
			let type = options.type || 1
			uni.setNavigationBarTitle({
				title: options.typeText
			})
			this.setData({
				colors: app.globalData.newColor,
				goodData: goodData,
				type: type
			});
		},

		/**
		 * 生命周期函数--监听页面初次渲染完成
		 */
		onReady: function() {},

		/**
		 * 生命周期函数--监听页面显示
		 */
		onShow: function() { //需要获取存储的取件地址和收件地址
			if (getPickaddress()) {
				this.Pickaddress = getPickaddress()
			}
			if (getToaddress()) {
				this.Toaddress = getToaddress()
			}
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
			setCurrent(index) {
				let remark = this.remarkList[index];
				remark.current = !remark.current
				let data = 'remarkList[' + index + ']';
				this.setData({
					[data]: remark
				});
				let arr = [];
				this.remarkList.forEach(e => {
					if (e.current == true) {
						arr.push(e);
					}
				});
				console.log(arr);
			},
			onChoose() {
				uni.showActionSheet({
					title: "选择上传类型",
					itemList: ['图片', '视频'],
					success: (res) => {
						if (res.tapIndex == 0) {
							this.chooseImages()
						} else {
							this.chooseVideo()
						}
					}
				})
			},
			chooseImages() { //上传图片
				let that = this;
				uni.chooseImage({
					//该方法是调出选择图片的方法
					count: 1, //数量限制
					sizeType: ['original', 'compressed'], //可选 原图 或缩略图
					success: function(res) {
						//返回的值为本地的图片的链接
						// 这里模拟接口向imgUrl 里添加图片  后期调用接口时参照该方法
						if (that.imgUrl.length >= 3) { //最多上传3张 超出了提醒
							uni.showToast({
								title: '最多上传3个',
								icon: 'none'
							})
						} else { //模拟上传图片
							let img = {
								url: '/static/images/goods/four.jpg',
								type: 1
							}
							that.imgUrl.push(img)
						}
					}
				});
			},
			chooseVideo() { //上传视频  
				let that = this;
				uni.chooseVideo({
					count: 1,
					sourceType: ['camera', 'album'],
					success: function(res) {
						console.log(res) //如果需要对视频的长度和大小做判断 在此处进行获取和处理
						// 下面是模拟上传视频 ↓
						if (that.imgUrl.length >= 3) { //最多上传3张 超出了提醒
							uni.showToast({
								title: '最多上传3个',
								icon: 'none'
							})
						} else { //模拟上传视频
							/**
							 *  ***重点注意 
							 *  视频的封面图因为需要做多端兼容 并且只允许是网络图片
							 *  所有建议是上传视频给后端之后，然后由后端对视频进行截取
							 * 	建议截取视频的第5帧来生成图片，并返回给前端
							 *  下面的poster是模拟后台返回的封面
							 */
							let video = {
								url: 'https://fzdz.soft.haoyangsoft.com/uploads/system/videos/20200813/6c819d24ee6868aee33e150c4333329b.mp4',
								type: 2,
								poster: 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1603080909940&di=ac10c5f2c952dd1b40441bb696c55a88&imgtype=0&src=http%3A%2F%2Fn.sinaimg.cn%2Fsinacn%2Fw640h640%2F20180127%2F369b-fyqzcxh1087346.jpg'
							}
							that.imgUrl.push(video)

						}
					}
				});
			},
			delImg(index) {
				//删除图片
				this.imgUrl.splice(index, 1);
			},
			previewImg(url){ //预览图片
				let arr = []
				arr[0] = url
				uni.previewImage({
					urls:arr
				})
			},
			onshowVideo(video) { //预览视频
			this.videos = video
			// #ifndef H5
			this.showVideo = true
			// #endif
			// #ifdef H5
			// h5 在真机上测试
			if(this.platform == 'android'){ //判断是安卓还是ios来对视频做适配
				this.isH5 = true
				this.newVideo.play()
			}else{
				this.showVideo = true
			}
			// #endif
			},
			hideShow() { //隐藏预览视频
				this.showVideo = false
			},
			ondefault() {
				// 抛弃的方法
			},
			setReturn() { //设置返回方式
				uni.showActionSheet({
					title: "选择返回方式",
					itemList: ['上门取件', '到店邮寄'],
					success: (res) => {
						this.types = res.tapIndex == 0 ? '上门取件' : '到店邮寄'
						this.tapIndex = res.tapIndex
					}
				})
			},
			openPopup() { //打开选择时间弹窗
				this.shows = true
			},
			onClose() {
				this.shows = false
			},
			setLocation(status) { //0 :设置取件地址   1 :设置收件地址  根据不同的status传递不同的地址
				let address = status == 0 ? this.Pickaddress : this.Toaddress
				uni.navigateTo({
					url: '/pages/views/order/location/location?status=' + status + '&address=' + JSON.stringify(address)
				})
			},
			onComplete(value) { //设置取货时间
				console.log('取货时间', value)
				this.pickTime = value
			},
			onsubmit(){
				uni.showToast({
					title:'提交成功'
				})
				setTimeout(()=>{
					uni.navigateBack({
						delta:2
					})
				},1500)
			}
		}
	};
</script>
<style lang="scss" scoped>
	page {
		background-color: #FFFFFF;
	}

	.cencal_order {
		padding: 20upx 4%;
		background-color: #fff;
	}

	.goods_data {
		display: flex;
		align-items: center;
		justify-content: flex-start;
		overflow: hidden;
		background-color: #FFFFFF;

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
				overflow: hidden;
				font-weight: bold;
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
				text-align: right;
				color: #999;
				margin-top: 5upx;
			}
		}
	}

	.youhui {
		height: 40upx;
		line-height: 40upx;
		padding: 20upx 0;
		border-bottom: 1upx solid #f2f2f2;
		box-sizing: content-box;

		.text1 {
			font-size: 28upx;
			color: #333333;
		}

		.text2 {
			float: right;
			color: #999999;
			font-size: 28upx;
			margin-right: 5upx;
			margin-top: 2upx;
		}

		.text3 {
			font-size: 24upx;
			color: #999999;
			margin-left: 10upx;
		}

		image {
			float: right;
			width: 12upx;
			height: 22upx;
			margin-top: 12upx;
			margin-left: 10upx;
		}
	}

	/* 预览视频弹窗 */
	.mask {
		width: 100%;
		height: 100%;
		position: fixed;
		top: 0;
		left: 0;
		background-color: rgba(0, 0, 0, .8);
		z-index: 910;
	}

	.previewvideo {
		width: 100vw;
		height: 100vw;
		position: fixed;
		top: 50%;
		left: 0;
		transform: translateY(-50%);
		background-color: #000;
		z-index: 920;
		opacity: 1;
	}

	.close {
		display: flex;
		align-content: center;
		align-items: flex-end;
		position: absolute;
		top: 100upx;
		right: 20upx;
		z-index: 900;

		image {
			width: 50upx;
			height: 50upx;
			display: block;
			justify-content: center;
			margin-left: 30upx;
			margin-bottom: 20upx;
			border-radius: 50%;
			padding: 10upx;
			background-color: rgba(0, 0, 0, 0.2);
		}
	}

	.videos {
		height: 100vw;
		width: 100vw;
		z-index: 10;
		position: relative;

		video {
			width: 100%;
			height: 100%;
		}
	}

	.nowvideos {
		width: 100%;
		height: 100%;
		margin: 0 auto;
	}

	.img_box {
		overflow: hidden;
		padding: 20upx 0;

		.addImg {
			width: 184upx;
			height: 184upx;
			background: #f2f2f2;
			border-radius: 20upx;
			overflow: hidden;
			transition: all 0.3s;
			image {
				width: 51upx;
				height: 42upx;
				display: block;
				margin: 0 auto;
				margin-top: 45upx;
			}

			p {
				font-size: 24upx;
				font-family: Microsoft YaHei;
				font-weight: 400;
				color: rgba(255, 94, 102, 1);
				text-align: center;
				margin-top: 20upx;
			}

			&:active {
				transform: scaleX(0.96);
			}
		}
	}

	.img_list {
		width: 184upx;
		height: 184upx;
		border-radius: 20upx;
		float: left;
		margin-right: 30upx;
		position: relative;
		image,
		video {
			width: 100%;
			height: 100%;
			display: block;
		}

		video {
			position: relative;
			border-radius: 5upx;
			overflow: hidden;
			overflow: visible !important;

			.covers {
				//遮挡层
				width: 100%;
				height: 100%;
				position: absolute;
				top: 0;
				left: 0;
				z-index: 9990;
			}

			.imgs {
				width: 72upx;
				height: 72upx;
				position: absolute;
				top: 50%;
				left: 50%;
				z-index: 9999;
				transform: translate(-50%, -50%);
			}

			.video_close {
				width: 40upx;
				height: 40upx;
				position: absolute;
				display: block;
				top: -6upx;
				left: -6upx;
				border-radius: 50%;
				z-index: 9999;
			}
		}

		.close {
			width: 40upx;
			height: 40upx;
			position: absolute;
			box-sizing: border-box;
			top: -6upx;
			left: -6upx;
			border-radius: 50%;
		}
	}

	.other {
		margin-top: 30upx;
		box-shadow: 0upx 0upx 10upx #ddd;
		padding: 10upx 20upx;
		border-radius: 20upx;

		.remark {
			background-color: #F5F5F5;
			border-radius: 10upx;
			height: 200upx;
			padding: 20upx;
			margin-top: 20upx;

			textarea {
				font-size: 24upx;
				color: #797979;
				height: 100%;
			}
		}

		.textarea_p {
			font-size: 24upx;
			color: #797979;
		}

		.tag_box {
			display: flex;
			flex-wrap: wrap;
			justify-content: space-between;
			margin-top: 40upx;
		}

		.tag_box::after {
			content: '';
			width: 30%;
		}

		.tag_list {
			max-width: 24%;
			min-width: 24%;
			text-align: center;
			margin-bottom: 30upx;
		}

		.tag_list view {
			height: 60upx;
			line-height: 60upx;
			border-radius: 30upx;
			border: 1upx solid #ddd;
			font-size: 22upx;
			color: #303030;
		}

	}

	.address {
		margin-top: 30upx;
		box-shadow: 0upx 0upx 10upx #ddd;
		padding: 20upx;
		border-radius: 20upx;

		.address_type {
			height: 80upx;
			line-height: 80upx;
			display: flex;
			justify-content: space-between;

			.type_text {
				font-size: 28upx;
				color: #8D8D8D;
			}

			.type_right {
				font-size: 28upx;
				color: #000000;
				font-weight: bold;
				display: flex;
				align-items: center;

				.more {
					width: 40upx;
					height: 40upx;
					display: block;
					margin-left: 20upx;
				}
			}
		}

		.rule {
			background-color: #FCF9E5;
			padding: 20upx;
			font-size: 24upx;
			display: flex;
			align-items: center;
			justify-content: space-between;

			.rule_left {
				width: 70%;
				color: #8D8D8D;
			}

			.rule_right {
				color: #E1251B;
			}
		}

		.user_address {
			display: flex;
			align-items: center;
			justify-content: space-between;
			padding-bottom: 20upx;
			margin-top: 30upx;
			border-bottom: 1upx solid #EEEEEE;

			.u_a_top {
				height: 60upx;
				line-height: 60upx;
				font-size: 28upx;
				color: #000000;
				font-weight: bold;
				display: flex;
				align-content: center;

				.iconfont {
					font-weight: 500;
					margin-right: 20upx;
					font-size: 38upx;
					color: #666666;
				}

				.name {
					margin-right: 10upx;
					font-size: 30upx;
				}
			}

			.u_a_bottom {
				font-size: 24upx;
				color: #8D8D8D;
				margin-left: 55upx;
				margin-top: 10upx;
				overflow: hidden;
				white-space: nowrap;
				text-overflow: ellipsis;
			}

			image {
				width: 40upx;
				height: 40upx;
				display: block;
			}

			&:active {
				opacity: .8;
			}
		}

		.times {
			display: flex;
			align-items: center;
			justify-content: space-between;
			padding: 30upx 0;

			.rili {
				width: 35upx;
				height: 35upx;
				padding: 5upx;
				box-sizing: content-box;
			}

			.times_title {
				width: 84%;
				text-align: left;
				color: #000000;
			}

			.more {
				height: 40upx;
				width: 40upx;
				display: block;
			}

		}

		.m_a_title {
			font-size: 28upx;
			color: #8D8D8D;
			height: 80upx;
			line-height: 80upx;

			text {
				margin-left: 20upx;
				font-size: 22upx;
			}
		}
	}

	.contacts {
		margin-top: 30upx;
		box-shadow: 0upx 0upx 10upx #ddd;
		padding: 20upx;
		border-radius: 20upx;

		.user_cell {
			height: 80upx;
			line-height: 80upx;
			display: flex;
			align-items: center;

			image {
				width: 40upx;
				height: 40upx;
				display: block;
			}

			text {
				font-size: 28upx;
				color: #000000;
				font-weight: bold;
				margin-left: 20upx;
			}
		}
	}

	.tips {
		font-size: 24upx;
		color: #999999;
		height: 40upx;
		line-height: 40upx;
		margin-top: 100upx;
		text-align: center;
	}

	.btns {
		width: 100%;
		height: 80upx;
		line-height: 80upx;
		font-size: 30upx;
		color: #FFFFFF;
		text-align: center;
		margin: 20upx 0;
		border-radius: 8upx;

		&:active {
			opacity: .8;
		}
	}
</style>
