<template>
	<view class="example">
<!-- 		<view class="example-title">基本用法</view>
		<uni-steps :options="list1" :active="active" /> -->
		<view class="example-title">{{status}}</view>
		<uni-steps :options="list2" :active="active" direction="column" />
		<button type="primary" @click="change" v-if="status=='growing in progress'">status confirmation</button>
		<view v-if="status=='crop matured'" style="display: flex; justify-content: space-between;">
		<button class="chengshu" type="primary" @click="category">sale</button>
		<button class="chengshu" type="primary" @click="processing">processing</button>
		</view>
	</view>
</template>

<script>
	import uniSteps from '@/components/uni-steps/uni-steps.vue'

	export default {
		components: {
			uniSteps
		},
		data() {
			return {
				status: 'growing in progress',
				active: 0,
				list1: [{
					title: '事件一'
				}, {
					title: '事件二'
				}, {
					title: '事件三'
				}, {
					title: '事件四'
				}],
				list2: [
					{
					title: 'Sow. Choose the appropriate variety of wheat according to your needs, and place the seeds at a distance of 6-7 centimeters apart, based on radius.',
					desc: '2023-3-25'
				}, {
					title: 'Irrigation and fertilization. Irrigation helps the seeds to germinate and maintains soil moisture. After irrigation, fertilization can provide sufficient nutrients for the seedlings to grow quickly.', 
					desc: '2023-3-26'
				}, {
					title: 'Weeding and loosening the soil. After wheat germinates, grass and weeds will occupy the growing space. Weeding helps wheat maintain sufficient nutrition and growing space. Loosening the soil can increase soil looseness and improve its ability to absorb air and water.',
					desc: '2023-4-10’'
				}, {
					title: 'Fertilization and weeding. Repeat fertilization can increase wheat yield and improve its quality, while weeding can provide more growing space.',
					desc: '2023-4-20'
				},{
					title: 'Loosening the soil and pruning. Loosening the soil can make roots more stable, and pruning can help wheat maintain a good shape and improve plant quality.',
					desc: '2023-5-5'
				},{
					title: 'Harvesting. The harvest time of wheat varies depending on the variety and climate conditions. Before harvesting, it is necessary to check whether the wheat is mature and whether it has reached an appropriate moisture content.',
					desc: '2023-5-14'
				}]
			}
		},
		methods: {
			change() {
				if (this.active < this.list2.length - 1) {
					this.active += 1
					this.status = 'growing in progress'
					if(this.active == this.list2.length - 1){
						this.status = 'crop matured'
					}
				} else {
					this.active = 0
					this.status = 'growing in progress'
				}
			},
			category() {
				uni.switchTab({
				  url: '/pages/views/tabBar/category' 
				});
				
			},
			processing() {
				uni.navigateTo({
				  url: '/pages/views/home/JiaGong' 
				});
			}
		}
	}
</script>

<style>
	page {
		display: flex;
		flex-direction: column;
		box-sizing: border-box;
		background-color: #fff
	}

	view {
		font-size: 28upx;
		line-height: inherit
	}

	.chengshu {
		width: 40%;
		background-color: darkorange;
	}

	.example {
		padding: 0 30upx 30upx
	}

	.example-title {
		font-size: 32upx;
		line-height: 32upx;
		color: #777;
		margin: 40upx 25upx;
		position: relative
	}

	.example .example-title {
		margin: 40upx 0
	}
    .gui-button-round {
        display: inline-block;
/* 		position: absolute; 
		right: 5%; */
        background-color: rgba(255, 140, 0, 1);
        box-sizing: border-box;
        font-size: 1em;
        text-align: center;
        padding-left: 1.4em;
        color: #fff;
        font-weight: 500;
        border-color: #409eff;
        line-height: 1;
        white-space: nowrap;
        cursor: pointer;
        border: 1px solid #dcdfe6;
        -webkit-appearance: none;
        outline: none;
        margin: 0;
        transition: 2.1s;
        -moz-user-select: none;
        -webkit-user-select: none;
        -ms-user-select: none;
        padding-top: 0.8em;
        padding-right: 1.4em;
        padding-bottom: 0.8em;
        border-top-left-radius: 1.5em;
        border-bottom-left-radius: 1.5em;
        border-top-right-radius: 1.5em;
        border-bottom-right-radius: 1.5em;
    }
	.example-body {
		padding: 0 40upx
	}

	button {
		margin: 30upx;
	}
</style>