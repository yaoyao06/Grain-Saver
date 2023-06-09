<template>
    <!--ShouYehtmlStart-->

    <view id="defaultId1" class="  home">
        <!-- 顶部 -->
        <headers id="idQWj5vt" :colors="colors" :locations="locations" :swiperList="swiperList">
        </headers>
<!--        <banner id="idBV4JmK">
        </banner> -->
<!--        <map id="cf122c" class=" uLUgdMV" ids="cf122c" :latitude="latitude" :longitude="longitude" :markers="covers">
        </map> -->
        <!-- 热门标题 -->
		<position id="idmxirG9" class=" uCdTNdI" :colors="colors" >
		</position>
		<tuijian id="idmxirG9" class=" uCdTNdI" :colors="colors" >
		</tuijian>
		<!-- <list-cell icons="icon-zuji" linkUrl="/components/qingqing-steps/uni-steps" :rightshow="true" :colors="colors">推荐作物</list-cell> -->
        <hotstitle id="idmxirG9" class=" uCdTNdI" :colors="colors" >
        </hotstitle>
<!-- 		<wendajiqiren id="idmxirG9" class=" uCdTNdI" :colors="colors" >
		</wendajiqiren> -->
		
        <!-- <recommend id="idzfhWZR"  :colors="colors" :dataList="dataList" :loading="loading" :bottoms="bottoms" >
      </recommend> -->
        <!-- 右侧悬浮菜单栏 -->
        <suspension id="idRqFOFD" :scrollShow="scrollShow" :colors="colors">
        </suspension>
    </view>
    <!--ShouYehtmlEnd-->

</template>

<script>
    var app = getApp();
    import headers from '../../commponent/home/header';
    import classList from '../../commponent/home/classList';
    import notice from '../../commponent/home/notice';
    import column from '../../commponent/home/column';
    import banner from '../../commponent/home/banner';
	import tuijian from '../../commponent/home/tuijian';
    import hotstitle from '../../commponent/home/hotstitle';
	import position from '../../commponent/home/position';
	import wendajiqiren from '../../commponent/home/wendajiqiren';
    import recommend from '../../commponent/home/recommend';
    import suspension from '../../commponent/home/suspension';
	import listCell from "../../commponent/user/list-cell";
    import {
        getlocation
    } from '@/utils/auth.js'
    export default {
        data() {
            return {
                // insertData
                // ShouYeDataStart

                // colors
                colors: '',
                // locations
                locations: {},
                // swiperList
                swiperList: [{
                    // "img": "/static/images/swiper/swiper1.jpg"
					"img": "/static/imagesibm/Al_Assists_Food_Security.jpg"
                }, {
                    // "img": "/static/images/swiper/swiper2.jpg"
					"img": "/static/imagesibm/Intelligent_Caculatyon.jpg"
                }, {
                    // "img": "/static/images/swiper/swiper3.jpg"
					"img": "/static/imagesibm/Smart_Planting_Strategy.jpg"
                }],
                // latitude
                latitude: 39.909,
                // longitude
                longitude: 116.39742,
                // covers
                covers: [{
                    "latitude": 39.9085,
                    "longitude": 116.39747,
                    "iconPath": "../../../static/location.png"
                }, {
                    "latitude": 39.9,
                    "longitude": 116.39,
                    "iconPath": "../../../static/location.png"
                }],
                // dataList
                // dataList: [{
                //     "title": "DUNKINDONUTS唐恩都乐美国甜甜圈6个礼盒装 随机搭配6款",
                //     "type": 1,
                //     "goods_id": 201,
                //     "money": "35.90",
                //     "number": 1,
                //     "hmoney": "45.90",
                //     "img": "/static/images/goods/one.jpg",
                //     "youhui": true,
                //     "baoyou": false,
                //     "status": 1,
                //     "stock": 600,
                //     "sku": [{
                //         "sku_id": 1,
                //         "skuname": "口味",
                //         "child": []
                //     }],
                //     "skuArr": []
                // }, {
                //     "title": "真巧 巧克力涂层甜甜圈 早餐蛋糕手撕面包休闲小零食办公室小吃零嘴下午茶点心 500g甜甜圈（拉花款）",
                //     "type": 2,
                //     "goods_id": 202,
                //     "money": "29.9",
                //     "number": 75,
                //     "hmoney": "39.90",
                //     "img": "/static/images/goods/two.jpg",
                //     "youhui": false,
                //     "baoyou": true,
                //     "status": 0,
                //     "stock": 100,
                //     "sku": [{
                //         "sku_id": 1,
                //         "skuname": "口味",
                //         "child": [{
                //             "tagname": "500g甜甜圈（彩针款）",
                //             "id": 2021,
                //             "imgs": "http://img14.360buyimg.com/n1/jfs/t1/72185/1/7121/222065/5d5377d5E46e681fa/6f100c77965b9165.jpg",
                //             "money": "39.90"
                //         }, {
                //             "tagname": "500g甜甜圈（拉花款）",
                //             "id": 2022,
                //             "imgs": "http://img14.360buyimg.com/n1/jfs/t1/72191/2/6973/239664/5d5377d5Ef952d7d9/606e70d2b6dd44d2.jpg",
                //             "money": "39.90"
                //         }]
                //     }],
                //     "skuArr": [{
                //         "goods_sku_arr": ["2021"],
                //         "goods_sku_text": "500g甜甜圈（彩针款）",
                //         "img": "http://img14.360buyimg.com/n1/jfs/t1/72185/1/7121/222065/5d5377d5E46e681fa/6f100c77965b9165.jpg",
                //         "money": "39.90",
                //         "stock": 50
                //     }, {
                //         "goods_sku_arr": ["2022"],
                //         "goods_sku_text": "500g甜甜圈（拉花款）",
                //         "img": "http://img14.360buyimg.com/n1/jfs/t1/72191/2/6973/239664/5d5377d5Ef952d7d9/606e70d2b6dd44d2.jpg",
                //         "money": "39.90",
                //         "stock": 50
                //     }]
                // }, {
                //     "title": "钟薛高 钟意你系列 特牛乳*4片 丝绒可可*4片 半巧主义*2 冰淇淋生鲜雪糕 10片装",
                //     "type": 3,
                //     "goods_id": 203,
                //     "money": "152.00 ",
                //     "number": 1,
                //     "hmoney": "162.00",
                //     "img": "/static/images/goods/there.jpg",
                //     "youhui": true,
                //     "baoyou": true,
                //     "status": 0,
                //     "stock": 200,
                //     "sku": [],
                //     "skuArr": []
                // }, {
                //     "title": "农谣人 原味火山石烤肠1000g/约16根台式原味肠地道肠纯肉肠热狗肠台湾烤肠香肠烧烤肠半熟食火腿肠 台式原味地道肠1kg",
                //     "type": 6,
                //     "goods_id": 204,
                //     "money": "52.00 ",
                //     "number": 1,
                //     "hmoney": "99.00 ",
                //     "youhui": false,
                //     "baoyou": false,
                //     "stock": 100,
                //     "img": "/static/images/goods/six.jpg",
                //     "status": 0,
                //     "sku": [{
                //         "skuname": "口味",
                //         "sku_id": 1,
                //         "child": [{
                //             "tagname": "台式原味地道肠1kg",
                //             "id": 2041,
                //             "imgs": "http://img10.360buyimg.com/n1/jfs/t1/118993/11/329/175715/5e8ac0afE94234346/3ceb1344cf34d655.jpg",
                //             "money": "52.00 "
                //         }, {
                //             "tagname": "台式黑椒味地道肠1kg",
                //             "id": 2042,
                //             "imgs": "http://img11.360buyimg.com/n1/jfs/t1/114876/9/17594/220403/5f5ae35bEc7bb735b/bcf0c1017e86894c.png",
                //             "money": "53.50"
                //         }]
                //     }],
                //     "skuArr": [{
                //         "goods_sku_arr": ["2041"],
                //         "goods_sku_text": "台式原味地道肠1kg",
                //         "img": "http://img10.360buyimg.com/n1/jfs/t1/118993/11/329/175715/5e8ac0afE94234346/3ceb1344cf34d655.jpg",
                //         "money": "52.00",
                //         "stock": 50
                //     }, {
                //         "goods_sku_arr": ["2042"],
                //         "goods_sku_text": "台式黑椒味地道肠1kg",
                //         "img": "http://img11.360buyimg.com/n1/jfs/t1/114876/9/17594/220403/5f5ae35bEc7bb735b/bcf0c1017e86894c.png",
                //         "money": "53.50",
                //         "stock": 50
                //     }]
                // }, {
                //     "title": "巧妈妈 鸡蛋布甸 下午茶休闲零食儿童果冻布丁125g双层果酱味smzdm 4杯鸡蛋布甸（双层）",
                //     "type": 4,
                //     "goods_id": 205,
                //     "money": "25.80",
                //     "number": 1,
                //     "hmoney": 35,
                //     "img": "/static/images/goods/four.jpg",
                //     "youhui": true,
                //     "baoyou": false,
                //     "stock": 500,
                //     "status": 0,
                //     "skuArr": [{
                //         "goods_sku_arr": ["10", "40"],
                //         "goods_sku_text": "鸡蛋布旬 4杯装",
                //         "img": "/static/images/goods/four.jpg",
                //         "money": "25.80",
                //         "stock": 50
                //     }, {
                //         "goods_sku_arr": ["10", "50"],
                //         "goods_sku_text": "鸡蛋布旬 6杯装",
                //         "img": "/static/images/goods/four.jpg",
                //         "money": "32.80",
                //         "stock": 10
                //     }, {
                //         "goods_sku_arr": ["10", "60"],
                //         "goods_sku_text": "鸡蛋布旬 8杯装",
                //         "img": "/static/images/goods/four.jpg",
                //         "money": "52.80",
                //         "stock": 60
                //     }, {
                //         "goods_sku_arr": ["20", "60"],
                //         "goods_sku_text": "乳酸菌布甸（草莓酱 8杯装）",
                //         "img": "http://img11.360buyimg.com/n1/jfs/t1/97403/35/15115/138620/5e6eeae8E8dbb7c3b/90a57a2a3e696b80.jpg",
                //         "money": "52.80",
                //         "stock": 100
                //     }, {
                //         "goods_sku_arr": ["30", "50"],
                //         "goods_sku_text": "乳酸菌布甸（蓝莓酱 8杯装）",
                //         "img": "http://img12.360buyimg.com/n1/jfs/t1/127005/26/7147/367042/5f0eb18cE9efa12ea/1a8363f7ce5a06cb.jpg",
                //         "money": "32.80",
                //         "stock": 1300
                //     }],
                //     "sku": [{
                //         "sku_id": 1,
                //         "skuname": "口味",
                //         "child": [{
                //             "tagname": "鸡蛋布旬",
                //             "id": 10,
                //             "imgs": "/static/images/goods/four.jpg",
                //             "money": "25.80"
                //         }, {
                //             "tagname": "乳酸菌布甸（草莓酱）",
                //             "id": 20,
                //             "imgs": "http://img11.360buyimg.com/n1/jfs/t1/97403/35/15115/138620/5e6eeae8E8dbb7c3b/90a57a2a3e696b80.jpg",
                //             "money": "14.80"
                //         }, {
                //             "tagname": "乳酸菌布甸（蓝莓酱）",
                //             "id": 30,
                //             "imgs": "http://img12.360buyimg.com/n1/jfs/t1/127005/26/7147/367042/5f0eb18cE9efa12ea/1a8363f7ce5a06cb.jpg",
                //             "money": "30.80"
                //         }]
                //     }, {
                //         "sku_id": 2,
                //         "skuname": "数量",
                //         "child": [{
                //             "tagname": "4杯装",
                //             "id": 40,
                //             "imgs": "",
                //             "money": "25.80"
                //         }, {
                //             "tagname": "6杯装",
                //             "id": 50,
                //             "imgs": "",
                //             "money": "32.80"
                //         }, {
                //             "tagname": "8杯装",
                //             "id": 60,
                //             "imgs": "",
                //             "money": "52.80"
                //         }]
                //     }]
                // }, {
                //     "title": "草莓云南夏季草莓新鲜水果3斤礼盒装 露天种植现摘现发 3斤精品装（4盒顺丰空运）",
                //     "type": 5,
                //     "goods_id": 206,
                //     "money": "59.90",
                //     "number": 200,
                //     "hmoney": "70.90",
                //     "youhui": true,
                //     "baoyou": true,
                //     "img": "/static/images/goods/five.jpg",
                //     "status": 0,
                //     "stock": 140,
                //     "sku": [{
                //         "sku_id": 1,
                //         "skuname": "种类",
                //         "child": [{
                //             "tagname": "3斤精品装",
                //             "id": 2061,
                //             "imgs": "http://img10.360buyimg.com/n1/jfs/t1/71401/15/15968/470755/5ddb8ecaEe6a5ce65/140942226e7c7551.jpg",
                //             "money": "59.90"
                //         }, {
                //             "tagname": "5斤精品装",
                //             "id": 2062,
                //             "imgs": "http://img10.360buyimg.com/n1/jfs/t1/82339/35/16255/632261/5ddb8ecdE628ab494/cacc1d2241e9f65f.jpg",
                //             "money": "82.90"
                //         }]
                //     }],
                //     "skuArr": [{
                //         "goods_sku_arr": ["2061"],
                //         "goods_sku_text": "3斤精品装",
                //         "img": "http://img10.360buyimg.com/n1/jfs/t1/71401/15/15968/470755/5ddb8ecaEe6a5ce65/140942226e7c7551.jpg",
                //         "money": "59.90",
                //         "stock": 80
                //     }, {
                //         "goods_sku_arr": ["2062"],
                //         "goods_sku_text": "5斤精品装",
                //         "img": "http://img10.360buyimg.com/n1/jfs/t1/82339/35/16255/632261/5ddb8ecdE628ab494/cacc1d2241e9f65f.jpg",
                //         "money": "82.90",
                //         "stock": 60
                //     }]
                // }],
                // loading
                loading: true,
                // bottoms
                bottoms: '100',
                // scrollShow
                scrollShow: false
                // ShouYeDataEnd

            };
        },
        components: {
            headers,
            classList,
            notice,
            column,
            banner,
			tuijian,
            hotstitle,
			wendajiqiren,
            recommend,
            suspension,
			listCell,
			position
        },
        /**
         * 生命周期函数--监听页面加载
         */
        onLoad: function(options) {
            // #ifdef APP-PLUS
            this.bottoms = '0' //在APP下 规格弹窗的位置发生变化
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
            uni.setNavigationBarColor({ //设置标题栏颜色
                backgroundColor: app.globalData.newColor,
                frontColor: '#ffffff'
            });
            // #ifdef H5
            let locations = getlocation() //获取位置信息
            if (locations) {
                this.locations = locations
            }
            // #endif
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
        onReachBottom: function() {
            if (this.dataList.length >= 30) { //模拟上拉加载数据
                this.loading = false
                return
            }
            let data = this.dataList;
            setTimeout(() => {
                this.loading = true
                this.dataList.push(...data);
            }, 500)
        },

        /**
         * 用户点击右上角分享
         */
        onShareAppMessage: function() {},
        methods: {
            // insertMethod
            // ShouYeMethodStart
            // onPageScroll

            onPageScroll(e) {


                if (e.scrollTop >= 500) {
                    this.setData({
                        scrollShow: true
                    });
                } else {
                    this.setData({
                        scrollShow: false
                    });
                }


            }
            // ShouYeMethodEnd

        }
    };
</script>
<style scoped lang="scss">
    .ShouYecssStart {}

    .home {
        height: 21px;
        margin-bottom: 40rpx;
    }

    .uLUgdMV {
        width: 100%;
        height: 150px;
        top: 10px;
    }

    .uCdTNdI {
        top: 20px;
        position: relative;
    }

    .ShouYecssEnd {}
</style>

// ShouYeMountedStart

// ShouYeMountedEnd
// ShouYePropsStart

// ShouYePropsEnd
//importStart

//importEnd