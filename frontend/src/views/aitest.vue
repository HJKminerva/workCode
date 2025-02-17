<template>
  <div class="parent-container">
    <!-- <h1>父组件</h1> -->
    <ChildComponent>
      <!-- <div class="filled-content">这是来自父组件的内容，应该占满整个插槽。</div> -->
    </ChildComponent>
  </div>
</template>

<script>
import ChildComponent from '@/components/ChildComponent.vue';

export default {
  components: {
    ChildComponent
  }
};
</script>

<style>
.parent-container {
  width: 100vb; /* 父容器宽度 */
  height: 200vh; /* 父容器高度 */
  border: 2px solid blue;
  position: relative; /* 相对定位以便子组件可以完全占满 */
}
.filled-content {
  background-color: lightyellow; /* 内容的背景色 */
  flex: 1; /* 让内容占满整个父容器 */
  display: flex; /* 使内容内部的子元素可以灵活排列 */
  justify-content: center; /* 水平居中对齐 */
  align-items: center; /* 垂直居中对齐 */
}
</style>
