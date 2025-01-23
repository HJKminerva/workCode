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
    <section class="hj-container is-vertical">
      <header class="hj-header mainframe_header">
        <div class="pc_header_off" style="height: 60px !important; opacity: 1;">
          <!-- 顶部栏（上方顶部） -->
          <div class="header_top">
            <div class="header_top_left">
              <div class="appList_icon" @click="handleAppItemClick('应用列表')">
                <img src="../components/icons/logo2.svg" alt="应用列表图标">
              </div>
              <div class="logo">
                <img src="../assets/images/logo-yunlian.png" alt="图片">
                <div class="logo_text">兴发工业</div>
              </div>
            </div>
          </div>
        </div>
      </header>

      <!-- 应用列表展开的页面 -->
      <section class="hj-container mainframe_container" v-show="isVisible">
        <div class="mainframe_left">
          <div class="sidebar" id="mainframe_sidebar">
            <div class="top">
              <div class="sidebar_applist">
                <div class="sidebar_appItem" v-show="isVisible">智慧园区</div>
                <div class="sidebar_appItem" @click="handleAppItemClick('物联网')">物联网</div>
                <div class="sidebar_appItem" @click="handleAppItemClick('智慧农业')">智慧农业</div>
                <div class="sidebar_appItem" @click="handleAppItemClick('智慧交通')">智慧交通</div>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- 切换的内容 -->
      <div class="page" v-show="isVisible">
        <div class="left" id="test_left">
          <div class="top">
            <div class="hj-input hj-input-large hj-input-prefix">
              <div class="hj-input__wrapper" tabindex="-1">
                <span class="hj-input__prefix"></span>
                <input class="hj-input_inner" type="text" placeholder="搜索" autocomplete="off" tabindex="0" v-model="searchText">
              </div>
            </div>
          </div>
          <div class="bottom">
            <div class="leftList">
              <div class="virtual_list">
                <div class="virtual_body">
                  <!--2级项目-->
                  <div class="leftList_item">
                    <div class="leftList_item_inner active_left_item">
                      <div class="icon">
                        <div style="user-select: none;">
                          <div class="svg-icon_content" text="企业服务;null">企</div>
                        </div>
                      </div>
                      <div class="text">
                        <div class="vxp-ellipsis">园区通行</div>
                      </div>
                      <div class="rightIcon">
                        <img src="../assets/images/rightIcon_arrow.png" alt="箭头图标">
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <div class="rightList">
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<style scoped>
.page .left .bottom .leftList .leftList_item .leftList_item_inner.active_left_item {
  color: #ff6a00;
  background-color: #f3f5f9;
}

.page .left .bottom .leftList .leftList_item .leftList_item_inner .icon {
  width: 20px;
  height: 20px;
  margin-left: 25px;
}

.page .left .bottom .leftList .leftList_item .leftList_item_inner .rightIcon img {
  width: 16px;
  height: 16px;
  position: absolute;
  right: 10px;
}

.page .left .bottom .leftList .leftList_item .leftList_item_inner .text {
  width: 100px;
  margin-left: 18px;
  font-size: 14px;
  display: inline-flex;
  align-items: center;
}

.page .left .bottom .leftList .leftList_item .leftList_item_inner {
  display: flex;
  align-items: center;
  position: relative;
  height: 40px;
  cursor: pointer;
}

.page .left .bottom .leftList .leftList_item {
  height: 45px;
  width: 100%;
  padding-bottom: 5px;
  color: #7c8791;
}

.virtual_list .virtual_body {
  position: absolute;
  overflow: hidden;
  left: 0;
  width: 100%;
  height: 100%;
  display: inline-flex;
  flex-direction: column;
}

.virtual_list {
  height: 100%;
  width: 100%;
  position: relative;
  overflow: auto;
}

.page .left .bottom .leftList {
  height: 100%;
  width: 200px;
  overflow: auto;
  border-right: 1px solid #ebeef5;
}

.page .left .bottom {
  flex: 1;
  overflow: hidden;
  padding: 10px;
  display: flex;
}

.hj-input__wrapper {
  align-items: center;
  background-color: var(--hj-input-bg-color, var(--hj-fill-color-blank));
  background-image: none;
  border-radius: var(--hj-input-border-radius, var(--hj-border-radius-base));
  box-shadow: 0 0 0 1px var(--hj-input-border-color, var(--hj-border-color)) inset;
  cursor: text;
  display: inline-flex;
  flex-grow: 1;
  justify-content: center;
  padding: 1px 11px;
  transform: translateZ(0);
  transition: var(--hj-transition-box-shadow);
}

.hj-input__prefix {
  color: var(--hj-input-icon-color, var(--hj-text-color-placeholder));
  display: inline-flex;
  flex-shrink: 0;
  flex-wrap: nowrap;
  height: 100%;
  pointer-events: none;
  text-align: center;
  transition: all var(--hj-transition-duration);
  white-space: nowrap;
}

.page {
  position: fixed;
  top: 60px;
  left: 200px;
  width: 950px;
  height: calc(100% - 60px);
  background-color: #fff;
  z-index: 3001;
  border-top: 1px solid #ebeef5;
  display: flex;
  padding-top: 15px;
}

.page .left {
  width: 730px;
  min-width: 720px;
  height: 100%;
  border-right: 1px solid #ebeef5;
  display: flex;
  flex-direction: column;
}

.page .left .top {
  padding-left: 9px;
  padding-right: 22px;
  padding-bottom: 9px;
}

.hj-input_inner {
  --hj-input-inner-height: calc(var(--hj-input-height, 32px) - 2px);
  background: none;
  border: none;
  box-sizing: border-box;
  color: var(--hj-input-text-color, var(--hj-text-color-regular));
  flex-grow: 1;
  font-size: inherit;
  height: var(--hj-input-inner-height);
  line-height: var(--hj-input-inner-height);
  outline: none;
  padding: 0;
  width: 100%;
}

.hj-input-large {
  --hj-input-height: var(--hj-component-size-large);
  font-size: 14px;
}

.hj-input-large .hj-input__wrapper {
  padding: 1px 15px;
}

.logo img {
  width: 40px;
  height: 40px;
  min-width: 40px;
}

.logo_text {
  margin-left: 5px;
  font-size: 20px;
  font-weight: 700;
  color: #545c64;
  font-family: Microsoft JhengHei UI Bold, Microsoft JhengHei UI, sans-serif;
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
  flex: 1;
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
  transition: all 0.2s;
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
  flex: 1;
  overflow: auto;
}

.sidebar_applist {
  display: flex;
  flex-direction: column;
  font-size: 16px;
}

.sidebar_appItem {
  padding: 10px;
  cursor: pointer;
  transition: background-color 0.3s;
}

.sidebar_appItem:hover {
  background-color: #f0f0f0;
}
</style>