<template>
    <!--FenLeiErJiCaiDanhtmlStart-->

    <view id="defaultId1" class="towstage  " @touchmove.stop.prevent="moveHandle">
        <scroll-view id="idcZHAUr" :class="['left',showHeader == false?'left_h5':'left_app']" :scroll-y="true" scroll-with-animation :scroll-top="scrollTop">
            <view id="idUfJRxD" v-for="(item, index) in classList" :style="{color:current == index ?colors:''}" :class="'classTitle ' + (current == index ? 'actives':'')" class=" uewsoiw" :key="index" @tap="setCurrent(item, index)">
                <text id="idoB6tvj">
                    <view id="c9f000" class="uni-flex uni-row  " ids="c9f000">
                    </view>
                    {{item.name}}

                </text>
                <view id="idCE9rsZ" :style="'background-color:' + colors" class="classactive  " v-if="current == index">
                </view>
            </view>
        </scroll-view>
        <scroll-view id="idbQoUFa" :class="['right',showHeader == false?'right_h5':'right_app']" :scroll-y="true" :scroll-with-animation="true">
            <view id="idRuqJjP" :class="['screen',showHeader == false?'screen_h5':'screen_app']" v-if="hideShow == true">
                <view id="iddzSoc7" class="xiaoliang  " @tap="setPrice">
                    <text id="idBdR5vQ" class="name  ">price
                    </text>
                    <view id="idCuvmlv" class="icon  ">
                        <text id="id1udvZF" :style="'color:' + (Price == '0' ? colors :'')" class="iconfont icon-shangsanjiao  ">
                        </text>
                        <text id="idGk3FD7" :style="'color:' + (Price == '1' ? colors :'')" class="iconfont icon-xiasanjiao  ">
                        </text>
                    </view>
                </view>
<!--                <view id="idThIPM7" class="xiaoliang  " @tap="setSales">
                    <text id="idPwjCz9" class="name  ">销量
                    </text>
                    <view id="idiwoERZ" class="icon  ">
                        <text id="idv5U8Ve" :style="'color:' + (sales == '0' ? colors :'')" class="iconfont icon-shangsanjiao  ">
                        </text>
                        <text id="idv688Qz" :style="'color:' + (sales == '1' ? colors :'')" class="iconfont icon-xiasanjiao  ">
                        </text>
                    </view>
                </view> -->
            </view>
            <view id="id5uvSFi" class="place  " v-if="hideShow == true">
            </view>
            <view id="idVtoNRK" class="goods_list  " v-if="dataList.length !== 0">
                <view id="id2lToqC" v-for="(item, index) in dataList" class="goods_item  " :key="index" v-if="item.type == showlist">
					<!-- <view v-if="item.type == showlist"> -->
						<image id="idiNevkx" :src="item.img" @tap="jumpDetail" :data-item="item">
						</image>
						<view id="idpjDTQM" class="goods_right  ">
							<view id="id4p1aI5" class="goods_name  " @tap="jumpDetail" :data-item="item">{{item.title}}
							</view>
							<view id="idcXZiKF" class="numbers  ">
								<text id="idP1mMel" v-if="item.youhui == true">优惠券
								</text>
								<text id="idViu9Sv" v-if="item.baoyou == true">包邮
								</text>
							</view>
							<view id="idecgdLv" class="price  ">
								<text id="idwfKRPu" class="money  ">￥{{item.money}}/kg
								</text>
<!-- 								<text id="idWbtXxm" class="hx_money  ">￥{{item.hmoney}}
								</text> -->
								<button id="cc0bbd" class="  gui-button-round" type="button" @tap="addCart(item)">sale
								</button>
<!-- 								<text id="idT9oTaS" class="iconfont icon-gouwuche gouwuche  uTFJ2dp" @tap="addCart(item)">
									<button id="cc0bbd" class="  gui-button-round" type="button">出售
									</button>
								</text> -->
							</view>
							<view>
							<text id="idwfKRPu" class="distance  ">distance:{{item.distance}}/km
							</text>
							<view>
							<text id="idwfKRPu" class="distance  ">carbon emissions:{{item.tan}}kg
							</text>
							</view>
							</view>
						</view>
					</view>
                <!-- </view> -->
                <view id="idxhgqSM" class="nodata  ">—— bottom ——
                </view>
            </view>
            <view id="idLR2bM5" class="zanwu  " v-if="dataList.length == 0">
                <text id="idaouRZZ" class="iconfont icon-none  uAF5fbm">
                </text>
                <text id="idX6Bpd2" class="  uNXL8uS">暂无商品
                </text>
            </view>
        </scroll-view>
        <!-- 弹出规格选项 -->
        <sku id="idCQliW3" :skuList="nowList" :showModal="showModal" :colors="colors" @onhide="onhide" :bottoms="bottoms">
        </sku>
    </view>
    <!--FenLeiErJiCaiDanhtmlEnd-->

</template>

<script>
    import sku from '../public/sku.vue'
    export default {
        data() {
            return {
                // insertData
                // FenLeiErJiCaiDanDataStart

                // scrollTop
                scrollTop: 0,
                // Price
                Price: '',
                // sales
                sales: '',
                // nowList
                nowList: {},
				showlist: 1,
                // showModal
                showModal: false
                // FenLeiErJiCaiDanDataEnd

            };
        },

        components: {
            sku
        },
        props: {
            // FenLeiErJiCaiDanPropsStart

            // FenLeiErJiCaiDanPropsEnd

            // ErJiCaiDanPropsStart

            // ErJiCaiDanPropsEnd

            colors: {
                type: String
            },
            hideShow: {
                //控制是否显示筛选
                type: Boolean,
                default: true
            },
            classList: {
                type: Array
            },
            dataList: {
                type: Array
            },
            current: {
                type: Number,
                default: 0
            },
            showHeader: { //用来控制在APP下样式
                type: Boolean,
                default: false
            },
            bottoms: {
                type: String,
                default: '100'
            },
        },
        methods: {
            // insertMethod
            // FenLeiErJiCaiDanMethodStart
            // setCurrent
            setCurrent(item, index) {

				this.showlist = item.id
                //设置tab
                let scrollTop = index * 20;
                if (index <= 2) {
                    scrollTop = 0;
                }
                this.setData({
                    current: index,
                    scrollTop: scrollTop,
                });
                this.$emit('setTwo', item)


            }, // setPrice
            setPrice() {


                //价格排序
                let price = this.Price;
                /**
                 * 0 代表升序
                 * 1 代表降序
                 */
                if (price == '') {
                    this.setData({
                        Price: '0',
                        sales: ''
                    });
                } else if (price == '0') {
                    this.setData({
                        Price: '1'
                    });
                } else if (price == '1') {
                    this.setData({
                        Price: '0'
                    });
                }


            }, // setSales
            setSales() {


                //销量排序
                let sales = this.sales;
                /**
                 * 0 代表升序
                 * 1 代表降序
                 */
                if (sales == '') {
                    this.setData({
                        sales: '0',
                        Price: ''
                    });
                } else if (sales == '0') {
                    this.setData({
                        sales: '1'
                    });
                } else if (sales == '1') {
                    this.setData({
                        sales: '0'
                    });
                }


            }, // jumpDetail
            jumpDetail(e) {


                uni.navigateTo({
                    url: '/pages/views/goods/goodsDetails'
                });

            }, // addCart
            addCart(item) {


                this.nowList = item
                this.showModal = true


            }, // onhide
            onhide() {


                //隐藏规格对话框
                this.showModal = false


            }
            // FenLeiErJiCaiDanMethodEnd

        }
    };
</script>
<style scoped lang="scss">
    .FenLeiErJiCaiDancssStart {}

    .uewsoiw {
        box-sizing: border-box;
    }

    .uTFJ2dp {
        align-items: center;
    }

    .gui-button-round {
        display: inline-block;
		position: absolute; 
		right: 0%;
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

    .uAF5fbm {
        font-size: 32upx
    }
	.distance {
		font-size: 20upx;
		color: #999;
		margin-right: 20upx;
		padding-right: 5px;
	}
    .uNXL8uS {
        font-size: 24upx
    }

    .gui-button-round:active {
        transform: scale(0.75);
        box-shadow: 0px 0px 0.1em 0.4em rgba(180, 179, 179, 1);
    }

    .FenLeiErJiCaiDancssEnd {}











    @import "./twostage.scss";
</style>
// ErJiCaiDanMountedStart

// ErJiCaiDanMountedEnd
//importStart

//importEnd
// FenLeiErJiCaiDanMountedStart

// FenLeiErJiCaiDanMountedEnd