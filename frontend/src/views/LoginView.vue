<template>
  <div class="login-container">
    <div class="login-form">
      <h2>登录</h2>
      <form @submit.prevent="handleLogin">
        <div class="form-group">
          <label for="username">用户名</label>
          <input
            type="text"
            id="username"
            v-model="username"
            placeholder="请输入用户名"
            required
          />
        </div>
        <div class="form-group">
          <label for="password">密码</label>
          <input
            type="password"
            id="password"
            v-model="password"
            placeholder="请输入密码"
            required
          />
        </div>
        <button type="submit" class="login-button">登录</button>
      </form>
      <p class="register-link">
        没有账号？<router-link to="/register">立即注册</router-link>
      </p>
    </div>
  </div>
</template>

<script>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import axios from 'axios';

export default {
  setup() {
    const router = useRouter();
    const username = ref('');
    const password = ref('');
    console.log(username.value,password.value);
    const handleSubmit = async () => {
      console.log("LoginView.vue 被加载了4");
      try {
        const response = await axios.post("http://127.0.0.1:5000/login", {
          username: username.value,
          password: password.value,
        });

        if (response.status === 200) {
          alert("登录成功！");
          router.push({ name: '/' });
        } else {
          alert(response.data.message || "登录失败，请重试！");
        }
      } catch (error) {
        if (error.response) {
          alert(error.response.data.error || "用户名或密码错误");
        } else {
          console.error("请求未到达后端:", error);
          alert("网络错误，请检查后端服务");
        }
      }
    };

    return {
      username,
      password,
      handleSubmit,
    };
  },
};
</script>


<style scoped>
/* 居中容器 */
.login-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  background-color: #f5f5f5;
}

/* 登录表单样式 */
.login-form {
  width: 350px;
  padding: 20px;
  background: #ffffff;
  border-radius: 8px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

/* 表单组样式 */
.form-group {
  margin-bottom: 15px;
}

/* 标签样式 */
.form-group label {
  display: block;
  margin-bottom: 5px;
  font-weight: bold;
}

/* 输入框样式 */
.form-group input {
  width: 100%;
  padding: 8px;
  font-size: 14px;
  border: 1px solid #ccc;
  border-radius: 4px;
}

/* 登录按钮样式 */
.login-button {
  width: 100%;
  padding: 10px;
  font-size: 16px;
  color: #fff;
  background-color: #42b983;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.login-button:hover {
  background-color: #38a169;
}

/* 注册链接样式 */
.register-link {
  text-align: center;
  margin-top: 10px;
}
</style>