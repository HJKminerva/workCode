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
    <div class="applist_container">
        <slot>
            <div class="page" v-show="isVisible" >
                <div class="top">
                    <div class="hj-input hj-input--large hj-input--prefix searchInput">
                        <!--input-->
                        <!--prepend slot-->
                        <!--v-if-->
                        <div class="hj-input__wrapper" tabindex="-1">
                            <span class="hj-input__prefix">
                                <span class="hj-input__prefix-inner">
                                    <img src="../assets/images/searchIcon.svg" alt="搜索图标">
                                </span>
                            </span>
                            <input class="hj-input__inner" type="text" autocomplete="off" tabindex="0" placeholder="搜索应用" >
                        </div>
                        <!--append slot-->
                        <!--v-if-->
                    </div>
                </div>
                <div class="bottom">
                    <div class="left">
                        <div class="list">
                            <div class="virtual_list">
                                <div class="virtual_back" style="height: 360px;"></div>
                                <div class="virtual_body" style="top: 0px;">

                                    <!--默认分组-->
                                    <div class="myItem myItem_groupName">默认分组</div>
                                    <div class="myItem myItem_appList">
                                        <div class="appItem">
                                            <div class="icon">
                                                <div style="user-select: none;">
                                                    <div class="svg-icon_content" text="平台管控;null" style="display: flex; justify-content: center; align-items: center; cursor: pointer; height: 24px; width: 24px; line-height: 24px; font-size: 19.2px;">管</div>
                                                </div>
                                            </div>
                                            <div class="text">
                                                <div class="vxp-ellipsis" aria-describedby="vxp-ellipsis-0" style="z-index: inherit;">平台管控</div>
                                            </div>
                                            <div class="collect">
                                                <i class="hj-icon" style="color: rgb(255,106,0);">
                                                    <svg data-v-312386fd="" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024"><path fill="currentColor" d="M283.84 867.84 512 747.776l228.16 119.936a6.4 6.4 0 0 0 9.28-6.72l-43.52-254.08 184.512-179.904a6.4 6.4 0 0 0-3.52-10.88l-255.104-37.12L517.76 147.904a6.4 6.4 0 0 0-11.52 0L392.192 379.072l-255.104 37.12a6.4 6.4 0 0 0-3.52 10.88L318.08 606.976l-43.584 254.08a6.4 6.4 0 0 0 9.28 6.72z"></path></svg>
                                                </i>
                                                <i class="hj-icon" >
                                                    <svg data-v-312386fd="" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024"><path fill="currentColor" d="m512 747.84 228.16 119.936a6.4 6.4 0 0 0 9.28-6.72l-43.52-254.08 184.512-179.904a6.4 6.4 0 0 0-3.52-10.88l-255.104-37.12L517.76 147.904a6.4 6.4 0 0 0-11.52 0L392.192 379.072l-255.104 37.12a6.4 6.4 0 0 0-3.52 10.88L318.08 606.976l-43.584 254.08a6.4 6.4 0 0 0 9.28 6.72zM313.6 924.48a70.4 70.4 0 0 1-102.144-74.24l37.888-220.928L88.96 472.96A70.4 70.4 0 0 1 128 352.896l221.76-32.256 99.2-200.96a70.4 70.4 0 0 1 126.208 0l99.2 200.96 221.824 32.256a70.4 70.4 0 0 1 39.04 120.064L774.72 629.376l37.888 220.928a70.4 70.4 0 0 1-102.144 74.24L512 820.096l-198.4 104.32z"></path></svg>
                                                </i>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="myItem myItem_border">
                                        <div class="border"></div>
                                    </div>

                                    <!--运营支撑-->
                                    <div class="myItem myItem_groupName">运营支撑</div>
                                    <!---->
                                    <!---->
                                    <!---->
                                    <div class="myItem myItem_appList">
                                        <div class="appItem">
                                            <div class="icon">
                                                <div style="user-select: none;">
                                                    <div class="svg-icon_content" text="工匠云;null" style="display: flex; justify-content: center; align-items: center; cursor: pointer; height: 24px; width: 24px; line-height: 24px; font-size: 19.2px;">工</div>
                                                </div>
                                            </div>
                                            <div class="text">
                                                <div class="vxp-ellipsis" aria-describedby="vxp-ellipsis-0" style="z-index: inherit;">工匠云</div>
                                            </div>
                                            <div class="collect">
                                                <i class="hj-icon" style="color: rgb(255,106,0);">
                                                    <svg data-v-312386fd="" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024"><path fill="currentColor" d="M283.84 867.84 512 747.776l228.16 119.936a6.4 6.4 0 0 0 9.28-6.72l-43.52-254.08 184.512-179.904a6.4 6.4 0 0 0-3.52-10.88l-255.104-37.12L517.76 147.904a6.4 6.4 0 0 0-11.52 0L392.192 379.072l-255.104 37.12a6.4 6.4 0 0 0-3.52 10.88L318.08 606.976l-43.584 254.08a6.4 6.4 0 0 0 9.28 6.72z"></path></svg>
                                                </i>
                                                <i class="hj-icon" >
                                                    <svg data-v-312386fd="" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024"><path fill="currentColor" d="m512 747.84 228.16 119.936a6.4 6.4 0 0 0 9.28-6.72l-43.52-254.08 184.512-179.904a6.4 6.4 0 0 0-3.52-10.88l-255.104-37.12L517.76 147.904a6.4 6.4 0 0 0-11.52 0L392.192 379.072l-255.104 37.12a6.4 6.4 0 0 0-3.52 10.88L318.08 606.976l-43.584 254.08a6.4 6.4 0 0 0 9.28 6.72zM313.6 924.48a70.4 70.4 0 0 1-102.144-74.24l37.888-220.928L88.96 472.96A70.4 70.4 0 0 1 128 352.896l221.76-32.256 99.2-200.96a70.4 70.4 0 0 1 126.208 0l99.2 200.96 221.824 32.256a70.4 70.4 0 0 1 39.04 120.064L774.72 629.376l37.888 220.928a70.4 70.4 0 0 1-102.144 74.24L512 820.096l-198.4 104.32z"></path></svg>
                                                </i>
                                            </div>
                                        </div>
                                        <div class="appItem">
                                            <div class="icon">
                                                <div style="user-select: none;">
                                                    <div class="svg-icon_content" text="智慧能源;null" style="display: flex; justify-content: center; align-items: center; cursor: pointer; height: 24px; width: 24px; line-height: 24px; font-size: 19.2px;">智</div>
                                                </div>
                                            </div>
                                            <div class="text">
                                                <div class="vxp-ellipsis" aria-describedby="vxp-ellipsis-0" style="z-index: inherit;">智慧能源</div>
                                            </div>
                                            <div class="collect">
                                                <i class="hj-icon" style="color: rgb(255,106,0);">
                                                    <svg data-v-312386fd="" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024"><path fill="currentColor" d="M283.84 867.84 512 747.776l228.16 119.936a6.4 6.4 0 0 0 9.28-6.72l-43.52-254.08 184.512-179.904a6.4 6.4 0 0 0-3.52-10.88l-255.104-37.12L517.76 147.904a6.4 6.4 0 0 0-11.52 0L392.192 379.072l-255.104 37.12a6.4 6.4 0 0 0-3.52 10.88L318.08 606.976l-43.584 254.08a6.4 6.4 0 0 0 9.28 6.72z"></path></svg>
                                                </i>
                                                <i class="hj-icon" >
                                                    <svg data-v-312386fd="" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024"><path fill="currentColor" d="m512 747.84 228.16 119.936a6.4 6.4 0 0 0 9.28-6.72l-43.52-254.08 184.512-179.904a6.4 6.4 0 0 0-3.52-10.88l-255.104-37.12L517.76 147.904a6.4 6.4 0 0 0-11.52 0L392.192 379.072l-255.104 37.12a6.4 6.4 0 0 0-3.52 10.88L318.08 606.976l-43.584 254.08a6.4 6.4 0 0 0 9.28 6.72zM313.6 924.48a70.4 70.4 0 0 1-102.144-74.24l37.888-220.928L88.96 472.96A70.4 70.4 0 0 1 128 352.896l221.76-32.256 99.2-200.96a70.4 70.4 0 0 1 126.208 0l99.2 200.96 221.824 32.256a70.4 70.4 0 0 1 39.04 120.064L774.72 629.376l37.888 220.928a70.4 70.4 0 0 1-102.144 74.24L512 820.096l-198.4 104.32z"></path></svg>
                                                </i>
                                            </div>
                                        </div>
                                        <div class="appItem">
                                            <div class="icon">
                                                <div style="user-select: none;">
                                                    <div class="svg-icon_content" text="工匠云;null" style="display: flex; justify-content: center; align-items: center; cursor: pointer; height: 24px; width: 24px; line-height: 24px; font-size: 19.2px;">园</div>
                                                </div>
                                            </div>
                                            <div class="text">
                                                <div class="vxp-ellipsis" aria-describedby="vxp-ellipsis-0" style="z-index: inherit;">智慧园区</div>
                                            </div>
                                            <div class="collect">
                                                <i class="hj-icon" style="color: rgb(255,106,0);">
                                                    <svg data-v-312386fd="" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024"><path fill="currentColor" d="M283.84 867.84 512 747.776l228.16 119.936a6.4 6.4 0 0 0 9.28-6.72l-43.52-254.08 184.512-179.904a6.4 6.4 0 0 0-3.52-10.88l-255.104-37.12L517.76 147.904a6.4 6.4 0 0 0-11.52 0L392.192 379.072l-255.104 37.12a6.4 6.4 0 0 0-3.52 10.88L318.08 606.976l-43.584 254.08a6.4 6.4 0 0 0 9.28 6.72z"></path></svg>
                                                </i>
                                                <i class="hj-icon" >
                                                    <svg data-v-312386fd="" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024"><path fill="currentColor" d="m512 747.84 228.16 119.936a6.4 6.4 0 0 0 9.28-6.72l-43.52-254.08 184.512-179.904a6.4 6.4 0 0 0-3.52-10.88l-255.104-37.12L517.76 147.904a6.4 6.4 0 0 0-11.52 0L392.192 379.072l-255.104 37.12a6.4 6.4 0 0 0-3.52 10.88L318.08 606.976l-43.584 254.08a6.4 6.4 0 0 0 9.28 6.72zM313.6 924.48a70.4 70.4 0 0 1-102.144-74.24l37.888-220.928L88.96 472.96A70.4 70.4 0 0 1 128 352.896l221.76-32.256 99.2-200.96a70.4 70.4 0 0 1 126.208 0l99.2 200.96 221.824 32.256a70.4 70.4 0 0 1 39.04 120.064L774.72 629.376l37.888 220.928a70.4 70.4 0 0 1-102.144 74.24L512 820.096l-198.4 104.32z"></path></svg>
                                                </i>
                                            </div>
                                        </div>
                                    </div>

                                    <div class="myItem myItem_appList">
                                        <div class="appItem">
                                            <div class="icon">
                                                <div style="user-select: none;">
                                                    <div class="svg-icon_content" text="工匠云;null" style="display: flex; justify-content: center; align-items: center; cursor: pointer; height: 24px; width: 24px; line-height: 24px; font-size: 19.2px;">躬</div>
                                                </div>
                                            </div>
                                            <div class="text">
                                                <div class="vxp-ellipsis" aria-describedby="vxp-ellipsis-0" style="z-index: inherit;">躬铝智数</div>
                                            </div>
                                            <div class="collect">
                                                <i class="hj-icon" style="color: rgb(255,106,0);">
                                                    <svg data-v-312386fd="" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024"><path fill="currentColor" d="M283.84 867.84 512 747.776l228.16 119.936a6.4 6.4 0 0 0 9.28-6.72l-43.52-254.08 184.512-179.904a6.4 6.4 0 0 0-3.52-10.88l-255.104-37.12L517.76 147.904a6.4 6.4 0 0 0-11.52 0L392.192 379.072l-255.104 37.12a6.4 6.4 0 0 0-3.52 10.88L318.08 606.976l-43.584 254.08a6.4 6.4 0 0 0 9.28 6.72z"></path></svg>
                                                </i>
                                                <i class="hj-icon" >
                                                    <svg data-v-312386fd="" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024"><path fill="currentColor" d="m512 747.84 228.16 119.936a6.4 6.4 0 0 0 9.28-6.72l-43.52-254.08 184.512-179.904a6.4 6.4 0 0 0-3.52-10.88l-255.104-37.12L517.76 147.904a6.4 6.4 0 0 0-11.52 0L392.192 379.072l-255.104 37.12a6.4 6.4 0 0 0-3.52 10.88L318.08 606.976l-43.584 254.08a6.4 6.4 0 0 0 9.28 6.72zM313.6 924.48a70.4 70.4 0 0 1-102.144-74.24l37.888-220.928L88.96 472.96A70.4 70.4 0 0 1 128 352.896l221.76-32.256 99.2-200.96a70.4 70.4 0 0 1 126.208 0l99.2 200.96 221.824 32.256a70.4 70.4 0 0 1 39.04 120.064L774.72 629.376l37.888 220.928a70.4 70.4 0 0 1-102.144 74.24L512 820.096l-198.4 104.32z"></path></svg>
                                                </i>
                                            </div>
                                        </div>
                                        <div class="appItem">
                                            <div class="icon">
                                                <div style="user-select: none;">
                                                    <div class="svg-icon_content" text="智慧能源;null" style="display: flex; justify-content: center; align-items: center; cursor: pointer; height: 24px; width: 24px; line-height: 24px; font-size: 19.2px;">设</div>
                                                </div>
                                            </div>
                                            <div class="text">
                                                <div class="vxp-ellipsis" aria-describedby="vxp-ellipsis-0" style="z-index: inherit;">设备管理</div>
                                            </div>
                                            <div class="collect">
                                                <i class="hj-icon" style="color: rgb(255,106,0);">
                                                    <svg data-v-312386fd="" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024"><path fill="currentColor" d="M283.84 867.84 512 747.776l228.16 119.936a6.4 6.4 0 0 0 9.28-6.72l-43.52-254.08 184.512-179.904a6.4 6.4 0 0 0-3.52-10.88l-255.104-37.12L517.76 147.904a6.4 6.4 0 0 0-11.52 0L392.192 379.072l-255.104 37.12a6.4 6.4 0 0 0-3.52 10.88L318.08 606.976l-43.584 254.08a6.4 6.4 0 0 0 9.28 6.72z"></path></svg>
                                                </i>
                                                <i class="hj-icon" >
                                                    <svg data-v-312386fd="" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024"><path fill="currentColor" d="m512 747.84 228.16 119.936a6.4 6.4 0 0 0 9.28-6.72l-43.52-254.08 184.512-179.904a6.4 6.4 0 0 0-3.52-10.88l-255.104-37.12L517.76 147.904a6.4 6.4 0 0 0-11.52 0L392.192 379.072l-255.104 37.12a6.4 6.4 0 0 0-3.52 10.88L318.08 606.976l-43.584 254.08a6.4 6.4 0 0 0 9.28 6.72zM313.6 924.48a70.4 70.4 0 0 1-102.144-74.24l37.888-220.928L88.96 472.96A70.4 70.4 0 0 1 128 352.896l221.76-32.256 99.2-200.96a70.4 70.4 0 0 1 126.208 0l99.2 200.96 221.824 32.256a70.4 70.4 0 0 1 39.04 120.064L774.72 629.376l37.888 220.928a70.4 70.4 0 0 1-102.144 74.24L512 820.096l-198.4 104.32z"></path></svg>
                                                </i>
                                            </div>
                                        </div>
                                    </div>

                                    <div class="myItem myItem_border">
                                        <div class="border"></div>
                                    </div>
                                    
                                    <!--精益制造-->
                                    <div class="myItem myItem_groupName">精益制造</div>
                                    <div class="myItem myItem_appList">
                                        <div class="appItem">
                                            <div class="icon">
                                                <div style="user-select: none;">
                                                    <div class="svg-icon_content" text="平台管控;null" style="display: flex; justify-content: center; align-items: center; cursor: pointer; height: 24px; width: 24px; line-height: 24px; font-size: 19.2px;">管</div>
                                                </div>
                                            </div>
                                            <div class="text">
                                                <div class="vxp-ellipsis" aria-describedby="vxp-ellipsis-0" style="z-index: inherit;">平台管控</div>
                                            </div>
                                            <div class="collect">
                                                <i class="hj-icon" style="color: rgb(255,106,0);">
                                                    <svg data-v-312386fd="" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024"><path fill="currentColor" d="M283.84 867.84 512 747.776l228.16 119.936a6.4 6.4 0 0 0 9.28-6.72l-43.52-254.08 184.512-179.904a6.4 6.4 0 0 0-3.52-10.88l-255.104-37.12L517.76 147.904a6.4 6.4 0 0 0-11.52 0L392.192 379.072l-255.104 37.12a6.4 6.4 0 0 0-3.52 10.88L318.08 606.976l-43.584 254.08a6.4 6.4 0 0 0 9.28 6.72z"></path></svg>
                                                </i>
                                                <i class="hj-icon" >
                                                    <svg data-v-312386fd="" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024"><path fill="currentColor" d="m512 747.84 228.16 119.936a6.4 6.4 0 0 0 9.28-6.72l-43.52-254.08 184.512-179.904a6.4 6.4 0 0 0-3.52-10.88l-255.104-37.12L517.76 147.904a6.4 6.4 0 0 0-11.52 0L392.192 379.072l-255.104 37.12a6.4 6.4 0 0 0-3.52 10.88L318.08 606.976l-43.584 254.08a6.4 6.4 0 0 0 9.28 6.72zM313.6 924.48a70.4 70.4 0 0 1-102.144-74.24l37.888-220.928L88.96 472.96A70.4 70.4 0 0 1 128 352.896l221.76-32.256 99.2-200.96a70.4 70.4 0 0 1 126.208 0l99.2 200.96 221.824 32.256a70.4 70.4 0 0 1 39.04 120.064L774.72 629.376l37.888 220.928a70.4 70.4 0 0 1-102.144 74.24L512 820.096l-198.4 104.32z"></path></svg>
                                                </i>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="myItem myItem_border">
                                        <div class="border"></div>
                                    </div>


                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="right"></div>
                </div>
            </div>
        </slot>
    </div>
</template>

<style scoped>
.appList_container {
    flex: 1;
}
.hj-input__inner {
    --hj-input-inner-height: calc(var(--hj-input-height, 32px) - 2px);
    --webkit-appearance: none;
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

.hj-input--large .hj-input__inner {
    --hj-input-inner-height: calc(var(--hj-input-height, 40px) - 2px);
}
.hj-input__prefix-inner {
    align-items: center;
    display: inline-flex;
    justify-content: center;
    pointer-events: all;
}
.page .top .searchInput {
    width: 650px;
}
.hj-input--large {
    --hj-input-height: var(--hj-component-size-large);
    font-size: 14px;
}
.hj-input {
    --hj-input-text-color: var(--hj-text-color-regular);
    --hj-input-border: var(--hj-border);
    --hj-input-hover-border: var(--hj-border-color-hover);
    --hj-input-focus-border: var(--hj-color-primary);
    --hj-input-transparent-border: 0 0 0 1px transparent inset;
    --hj-input-border-color: var(--hj-border-color);
    --hj-input-border-radius: var(--hj-border-radius-base);
    --hj-input-bg-color: var(--hj-fill-color-blank);
    --hj-input-icon-color: var(--hj-text-color-placeholder);
    --hj-input-placeholder-color: var(--hj-text-color-placeholder);
    --hj-input-hover-border-color: var(--hj-border-color-hover);
    --hj-input-clear-hover-color: var(--hj-text-color-secondary);
    --hj-input-focus-border-color: var(--hj-color-primary);
    --hj-input-width: 100%;
    --hj-input-height: var(--hj-component-size);
    box-sizing: border-box;
    display: inline-flex;
    font-size: var(--hj-font-size-base);
    line-height: var(--hj-input-height);
    position: relative;
    vertical-align: middle;
    width: var(--hj-input-width);
}
.page .bottom .left .list .myItem_appList .appItem .text{
    width: 140px;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
    cursor: pointer;
    font-size: 14px;
    margin-left: 6px;
    font-family: Source Han Sans SC Normal Bold, Source Han Sans SC Normal, sans-serif;
    font-weight: 700;
    color: #070707;
    display: flex;
}
.page .bottom .left .list .myItem_appList .appItem{
    width: 200px;
    height: 100%;
    margin-right: 12px;
    display: flex;
    align-items: center;
    padding: 5px;
    cursor: pointer;
}
.page .bottom .left .list .myItem_appList .appItem .icon {
    width: 30px;
    height: 30px;
    display: flex;
    align-items: center;
    justify-content: center;
}
.page .bottom .left .list .myItem_border .border {
    width: 100%;
    height: 1px;
    background-color: #5082f7;
}
.page .bottom .left .list .myItem_appList{
    display: flex;
    align-items: center;
}
.page .bottom .left .list .myItem{
    font-family: var(--font-siyuan);
    font-weight: 350;
    color: #ff6a00;
    padding-left: 12px;
    min-height: 36px;
    height: 36px;
    display: flex;
    align-items: center;
    font-size: 14px;
}
.page .bottom .left .list .myItem_groupName{
    color: #7c8791;
}

.page .bottom .left {
    width: 660px;
    min-width: 66px;
    height: 100%;
    border-right: 1px solid black;
}
.page .bottom .left .list {
    height: inherit;
    overflow: auto;
    display: flex;
    flex-wrap: wrap;
    align-content: flex-start;
}
.page .bottom .right {
    flex: 1;
    height: 100%;
    display: flex;
    border-left: 1px solid black;
    flex-direction: column;
}

.page .left .bottom .leftList .leftList_item .leftList_item_inner.active_left_item {
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
.virtual_list {
    height: 100%;
    width: 100%;
    position: relative;
    overflow: auto;
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
.np-input--large .hj-input__wrapper {
    padding:1px 15px;
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
hj-input__prefix-inner {
    align-items: center;
    display: inline-flex;
    justify-content: center;
    pointer-events: all;
}

.page {
    position: fixed;
    top: 60px;
    left: 0;
    width: 920px;
    height: calc(100% - 60px);
    background-color: #f5e6f2;
    z-index: 2009;
    transition: all 0.3s;
    border-top: 1px solid #0a0a0a;
    display: flex;
    flex-direction: column;
}

.page .top {
    padding: 6px;
    display: flex;
    align-items: center;
    height: 52px;
}
.page .buttom {
    display: flex;
    height: calc(100% - 52px);
    border-right: 1px solid #0a0a0a;
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