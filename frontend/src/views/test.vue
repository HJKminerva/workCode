<template>
    <div class="mainframe">
        <header class="mainframe_header"></header>
    </div>
</template>

<style scoped>
.mainframe {
    box-sizing: border-box;
    width: 100vw;
    height: 100vh; /* 确保高度设置正确 */
    display: flex;
    overflow: hidden;
}

.mainframe .mainframe_header {
    height: 60px;
    width: 100%;
    background-color: yellow;
    border: 1px solid red;
}
</style>
