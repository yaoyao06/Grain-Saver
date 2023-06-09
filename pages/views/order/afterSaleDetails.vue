<template>
	<view class="after_sale_details">
		<!-- 服务单步骤 -->
		<view class="top_step" :style="{background:colors}">
			<view class="mask">
			</view>
			<view class="step_box">
				<p class="status">{{details.order_type}}</p>
				<view class="step_list">
					<view class="top_x">
					</view>
					<view class="setp_all">
						<view class="setp_title" v-for="(item,index) in stepData" :key="index">
							<text class="dian" :style="{color:item.type==1 ||item.isNow==1 ?colors:'#eee'}">✓</text>
							<text class="text" :style="{fontWeight:item.isNow == 1?'bold':'none'}">{{item.name}}</text>
						</view>
					</view>
				</view>
			</view>
		</view>
		<!-- 服务介绍 -->
		<view class="service_box" @click="jumpStepDetail">
			<view class="left">
				<p class="left_js">服务已完成,感谢您的支持</p>
				<p class="left_des">问题描述：尊敬的客户您好,您的服务单已为您审核换货成功</p>
			</view>
			<image src="/static/images/home/right.png" mode=""></image>
		</view>
		<!-- 商品信息 -->
		<view class="goods_details">
			<p class="details_title">商品信息</p>
			<view class="goods_box">
				<image :src="details.img" class="cover" mode=""></image>
				<view class="goods_right">
					<p class="goods_name">{{details.title}}</p>
					<view class="sku">规格：{{details.goods_sku_text || '暂无规格'}}</view>
					<view class="price">
						<view class="t1">￥{{details.money}}</view>
						<view class="t3">
							x{{details.number}}
						</view>
					</view>
				</view>
			</view>
		</view>
		<!-- 服务单信息 -->
		<view class="service_details">
			<view class="cell_box">
				<text class="cell_text">服务单号</text>
				<text class="cell_content">{{serviceData.service_no}}</text>
				<text class="cell_btn" @click="onCopy(serviceData.service_no)">复制</text>
			</view>
			<view class="cell_box">
				<text class="cell_text">申请时间</text>
				<text class="cell_content">{{serviceData.create_time}}</text>
			</view>
			<view class="cell_box">
				<text class="cell_text">服务类型</text>
				<text class="cell_content">{{serviceData.fw_type}}</text>
			</view>
			<view class="cell_box">
				<text class="cell_text">商品退回</text>
				<text class="cell_content">{{serviceData.th_type}}</text>
			</view>
			<view class="cell_box">
				<text class="cell_text">取件地址</text>
				<text class="cell_content">{{serviceData.qj_address}}</text>
			</view>
			<view class="cell_box">
				<text class="cell_text">收货地址</text>
				<text class="cell_content">{{serviceData.sh_address}}</text>
			</view>
			<view class="cell_box">
				<text class="cell_text">联系人</text>
				<text class="cell_content">{{serviceData.realname}}</text>
			</view>
		</view>
		<view class="del_btn">
			<text @click="delService">删除服务单</text>
		</view>
		<loading v-if="isShow == true"></loading>
	</view>
</template>

<script>
	var app = getApp();
	import loading from "../../commponent/public/loading";
	export default {
		components:{
			loading
		},
		data(){
			return{
				colors:'',
				isShow: true,
				details:{},
				stepData:[  //该数据为后台返回 数据格式如此
					/**
					 * isNow：1 代表当前step 走到了这一步
					 * type：1 代表当前该步骤已经完成
					 */
					{step_id: 1, name:'提交申请',isNow:0, type: 1},
					{step_id: 2, name:'商家审核',isNow:0, type: 1},
					{step_id: 3, name:'商家收货',isNow:0,type:1},
					{step_id: 4, name:'换新',isNow:0, type: 1},
					{step_id: 5, name:'完成',isNow:1, type: 1},
				],
				serviceData:{
					service_no:'782260533',
					create_time:'2020-05-09 20:01:48',
					fw_type:'换货', //服务类型
					th_type:'上门取件', //取货类型
					qj_address:'安徽省合肥市包河区望湖街道马鞍山路',//取货地址
					sh_address:'安徽省合肥市包河区望湖街道马鞍山路', //收货地址
					realname:'反转'
				}
			}
		},
		onLoad(options) {
			this.setData({
				colors: app.globalData.newColor,
				details: JSON.parse(options.details) //这里是模拟的数据 正常使用时是调用接口根据服务单Id来获取
			});
			setTimeout(() => {
				this.setData({
					isShow: false
				});
			}, 600);
		},
		methods:{
			delService(){
				uni.showModal({
					title:'确认要删除该服务单吗?',
					confirmColor: this.colors,
					success: (res) => {
						if(res.confirm){
							console.log('删除订单')
						}
					}
				})
			},
			onCopy(value){ //复制内容
				// #ifdef H5
				var input = document.createElement('input'); // 直接构建input
				input.value = value; // 设置内容
				document.body.appendChild(input); // 添加临时实例
				input.select(); // 选择实例内容
				document.execCommand('Copy'); // 执行复制
				document.body.removeChild(input); // 删除临时实例
				uni.showToast({
					title:'复制成功~',
					icon:'none'
				})
				// #endif
				// #ifndef H5
				uni.setClipboardData({
					data:value,
					success:function(){
						uni.showToast({
							title:'复制成功~',
							icon:'none'
						})
					}
				})
				// #endif
			},
			jumpStepDetail(){ //进度详情
				uni.navigateTo({
					url:'/pages/views/order/stepDetails'
				})
			}
		}
	}
</script>

<style lang="scss" scoped>
	.top_step{
		height: 240upx;
		background-color: pink;
		position: relative;
		.mask{
			width: 100%;
			height: 100%;
			background: linear-gradient(to right,rgba(255,255,255,.1),rgba(255,255,255,.2));
		}
		.step_box{
			width: 100%;
			height: 100%;
			position: absolute;
			top: 0;
			left: 0;
			padding: 20upx 40upx;
			.status{
				height: 60upx;
				line-height: 60upx;
				color: #FFFFFF;
				font-size: 32upx;
				font-weight: bold;
			}
			.step_list{
				margin-top: 30upx;
				display: inline-block;
				.top_x{
					height: 4upx;
					background-color: #FFFFFF;
				}
				.setp_all{
					display: flex;
					align-items: center;
					.setp_title{
						transform: translateY(-18upx);
						margin-right: 40upx;
						.dian{
							width: 30upx;
							height: 30upx;
							display: block;
							background-color: #FFFFFF;
							border-radius: 50%;
							margin: 0 auto;
							text-align: center;
							line-height: 30upx;
							font-size: 26upx;
						}
						.text{
							font-size: 24upx;
							color: #FFFFFF;
							display: block;
							height: 40upx;
							line-height: 40upx;
							margin-top: 10upx;
						}
						&:first-of-type{
							.dian{
								margin-left: 0;
							}
						}
						&:last-of-type{
							margin-right: 0;
							.dian{
								margin-left: 100%;
								transform: translateX(-100%);
							}
						}
					}
				}
			}
		}
	}
	.service_box{
		padding: 30upx;
		background-color: #FFFFFF;
		margin: 0 20upx;
		transform: translateY(-50upx);
		border-radius: 15upx;
		display: flex;
		align-items: center;
		.left{
			.left_js{
				height: 60upx;
				line-height: 60upx;
				color: #000000;
				font-weight: bold;
			}
			.left_des{
				height: 40upx;
				width: 90%;
				line-height: 40upx;
				font-size: 24upx;
				overflow: hidden;
				text-overflow: ellipsis;
				white-space: nowrap;
			}
		}
		image{
			width: 40upx;
			height: 40upx;
			display: block;
		}
	}
	.goods_details{
		padding: 30upx;
		background-color: #FFFFFF;
		margin: 0 20upx;
		transform: translateY(-25upx);
		border-radius: 15upx;
		.details_title{
			font-size: 30upx;
			color: #999999;
			font-weight: bold;
			height: 40upx;
			line-height: 40upx;
		}
		.goods_box{
			display: flex;
			align-items: center;
			margin-top: 10upx;
			.cover{
				height: 140upx;
				width: 140upx;
				display: block;
				margin-right: 20upx;
				border-radius: 8upx;
			}
			.goods_right{
				flex: 1;
				.goods_name{
					font-size: 24upx;
					color: #000;
					display: -webkit-box;
					-webkit-box-orient: vertical;
					-webkit-line-clamp: 2;
					overflow: hidden;
				}
				.sku {
					height: 40upx;
					line-height: 40upx;
					font-size: 24upx;
					border-radius: 8upx;
					padding: 0 10upx;
					color: #A7A7A7;
					margin-top: 5upx;
					background-color: #F7F7F7;
				}
				
				.price {
					width: 100%;
					display: flex;
					align-items: center;
					height: 40upx;
					line-height: 40upx;
					margin-top: 5upx;
					position: relative;
					.t1 {
						font-size: 30upx;
						display: block;
						color: $mycolor;
					}
					.t2 {
						font-size: 24upx;
						margin-left: 15upx;
						display: block;
						color: #C5C5C5;
						text-decoration: line-through;
					}
					
					.t3 {
						float: right;
						font-size: 28upx;
						color: #999;
						position: absolute;
						right: 0upx;
						top: 0;
					}
				}
				
				.goods_other{
					display: flex;
					align-items: center;
					height: 50upx;
					line-height: 50upx;
					margin-top: 15upx;
					font-size: 24upx;
					color: #000000;
					.goods_price,.number{
						margin-right: 30upx;
						text{
							font-weight: bold;
							font-size: 30upx;
						}
					}
				}
			}
		}
	}
	.service_details{
		padding: 30upx;
		background-color: #FFFFFF;
		margin: 0 20upx;
		border-radius: 15upx;
		.cell_box{
			display: flex;
			margin: 30upx 0;
			.cell_text{
				font-size: 28upx;
				color: #8d8d8d;
				width: 120upx;
			}
			.cell_content{
				margin-left: 30upx;
				font-size: 26upx;
				color: #000000;
				flex: 1;
				line-height: 36upx;
			}
			.cell_btn{
				padding: 5upx 26upx;
				border: 1upx solid #ddd;
				margin-left: 30upx;
				border-radius: 30upx;
				font-size: 24upx;
				color: #202020;
				&:active{
					opacity: .8;
				}
			}
		}
	}
	.del_btn{
		font-size: 24upx;
		color: #8d8d8d;
		height: 160upx;
		line-height: 100upx;
		text-align: center;
		padding-top: 20px;
		text{
			padding: 10upx 20upx;
			border-radius: 30upx;
			border: 1upx solid #ddd;
			&:active{
				opacity: .8;
			}
		}
	}
</style>
<style>
	page{
		background-color: #F8F8F8;
	}
</style>
