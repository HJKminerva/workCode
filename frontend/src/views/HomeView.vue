<template>
  <body>
    <div class= "mainframe">
      <section class="hj-container is-vertical">
        <header class="hj-header mainframe_header">
          <div class="pc_header_off" style="height: 60px !important;opacity: 1;">
            <div class="header_top">
                <div class="header_top_left">
                  <div class="appList_icon">
                    <img src="../components/icons/logo2.svg" alt="">
                  </div>
                  <div>
                    <div class="logo">
                      <img src="../assets/img/logo-yunlian.png" alt="图片">
                      <div class="logo_text">兴发工业</div>
                    </div>
                  </div>
                </div>
                <!-- <div class="header_right">
                  <div class="header_right_item">登录</div>
                </div>  -->
            </div>
          </div>
        </header>
        
        <section class= "hj-container mainframe_container">
          <div class="mainframe_left">
            <div class="sidebar" id = "mainframe_sidebar">
              <div class="top">
                <div class="sidebar_applist">
                  <div class="sidebar_appItem" @click="handleAppItemClick('智慧园区')">智慧园区</div>
                  <div class="sidebar_appItem" @click="handleAppItemClick('物联网')">物联网</div>
                  <div class="sidebar_appItem" @click="handleAppItemClick('智慧农业')">智慧农业</div>
                  <div class="sidebar_appItem" @click="handleAppItemClick('智慧交通')">智慧交通</div>
                </div>
              </div>
            </div>
          </div>
        </section>
      </section>
    </div>
  </body>

</template>

<script>
export default {
  name: 'MainFrameLeft',
  methods: {
    handleAppItemClick(item) {
      console.log('点击了:', item);
      // 这里可以添加跳转逻辑或触发事件
    }
  }
};
</script>

<style scoped>
.logo img {
  width:40px;
  height: 40px;
  min-width: 40px;
}
.logo_text {
  margin-left: 5px;
  font-size: 20px;
  font-weight: 700;
  color: #545c64;
  font-family: Microsoft JhengHei UI Bold, Microsoft JhengHei UI, Microsoft JhengHei UI, sans-serif;
  overflow: hidden;
  text-overflow: ellipsis;
  display: -webkit-box;
  --webkit-line-clamp: 1;
  --webkit-box-orient: vertical;
}
.logo {
  width: 140px;
  display: flex;
  align-items: center;
  justify-content: center;
  height: 100%;
  border-right: 1px solid #e6e6e6;

}
.appList_icon {
  width: 60px;
  background-color: #ff6a00;
  height: 100%;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
}
.mainframe {
  box-sizing: border-box;
  width: 100vw;
  height: 100vh;
  max-width: 100vw;
  display: flex;
  overflow: hidden;
}
.hj-container {
  box-sizing: border-box;
  display: flex;
  flex:  1;
  flex-basis: auto;
  min-width: 0;
}
.hj-container.is-vertical {
  flex-direction: column;
}
.hj-header {
  --hj-header-padding: 0 20px;
  --hj-header-height: 60px;
  flex-shrink: 0;
}
.mainframe_header {
  padding: 0 !important;
  height: auto;
  box-sizing: border-box;
  transition: all .2s;
  overflow: hidden;
}
.header_top {
  height: 60px;
  background-color: #fff;
  display: flex;
  align-items: center;
}
.header_top .header_top_left {
  height: 100%;
  background-color: #fff;
  display: flex;
  align-items: center;
}
.mainframe_container {
  overflow: auto;
}
.mainframe_left {
  box-sizing: border-box;
  border: 1px solid rgb(218, 218, 218);
  position: relative;
  width: 200px;
  display: flex;
}

.sidebar {
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
}

.sidebar .top {
  flex: 1; /* 如果不需要占满空间，可以改为固定高度或移除 */
  overflow: auto;
}

.sidebar_applist {
  display: flex;
  flex-direction: column; /* 菜单项垂直排列 */
  font-size: 16px;
}

.sidebar_appItem {
  padding: 10px; /* 增加内边距，提升可读性 */
  cursor: pointer; /* 添加鼠标悬停效果 */
  transition: background-color 0.3s; /* 添加过渡效果 */
}

.sidebar_appItem:hover {
  background-color: #f0f0f0; /* 鼠标悬停时背景色变化 */
}
</style>