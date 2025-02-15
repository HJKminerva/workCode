<script>
export default {
    name: 'appList',
    data() {
        return {
            isVisible: true // 初始状态为显示
        };
    },
    methods: {
        handleAppItemClick(item) {
            console.log('点击了:', item);
            this.isVisible = !this.isVisible; // 切换显示状态
        }
    }
};
</script>

<template>
    <div class="mainframe">
        <header class="mainframe_header"></header>
        <section class="container">
            <div class="mainframe_left">
                <div class="sidebar">
                </div>
                <div class="page">
                    <div class="left">
                        <div class="top"></div>
                        <div class="bottom">
                            <div class="leftList"></div>
                            <div class="rightList">右侧内容</div>
                        </div>
                    </div>
                    <div class="right">page_right</div>
                </div>
            </div>
        </section>
    </div>
</template>

<style scoped>
.page .right {
    flex: 1;
    background-color: rgb(2, 9, 116);
}

.page .left .bottom .rightList {
    flex: 1;
    background-color: rgb(158, 243, 79);
    /* flex-direction: row; */
}

.page .left .bottom .leftList {
    width: 200px;
    height: 100%;
    background-color: rgb(228, 97, 108);
}

.page .left .bottom {
    flex: 1;
    width: 100%;
    height: 100%;
    background-color: rgba(151, 92, 233, 0.349);
    display: flex;
}

.page .top {
    padding: 6px;
    height: 52px;
    width: 100%;
    background-color: aqua;
}

.page .left {
    width: 730px;
    min-width: 720px;
    height: 100vh;
    background-color: rgb(235, 121, 174);
    border-right: 1px solid #ebeef5;
    display: flex;
    flex-direction: column;
}

.page {
    position: fixed;
    top: 60px;
    left: 200px;
    width: 920px;
    height: calc(100% - 60px);
    background-color: #f5e6f2;
    z-index: 2009;
    transition: all 0.3s;
    border-top: 1px solid #0a0a0a;
    display: flex;
    flex-direction: row;
}

.mainframe {
    box-sizing: border-box;
    width: 100vw;
    height: 100vh;
    height: 100dvh;
    max-width: 100vw;
    display: flex;
    flex-direction: column;
    flex-shrink: 0;
    overflow: hidden;
}

.mainframe .mainframe_header {
    height: 60px;
    width: 100%;
    background-color: yellow;
    flex-shrink: 0;
}

.mainframe .container {
    flex: 1;
    background-color: rgb(243, 179, 243);
}

.mainframe_left {
    width: 200px;
    height: 100vh;
    background-color: rgb(179, 243, 179);
    border-right: 1px solid black;
    overflow: auto;
}
</style>