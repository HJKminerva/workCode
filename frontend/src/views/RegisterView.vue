<template>
    <div class="register-container">
      <h2>用户注册</h2>
      <form @submit.prevent="handleSubmit" class="register-form">
        <div class="form-group">
          <label for="username">用户名：</label>
          <input 
            type="text" 
            id="username" 
            v-model="formData.username" 
            @input="validateUsername"
            placeholder="请输入用户名"
          />
          <span class="error-message" v-if="errors.username">{{ errors.username }}</span>
        </div>
  
        <div class="form-group">
          <label for="email">邮箱：</label>
          <input 
            type="email" 
            id="email" 
            v-model="formData.email" 
            @input="validateEmail"
            placeholder="请输入邮箱"
          />
          <span class="error-message" v-if="errors.email">{{ errors.email }}</span>
        </div>
  
        <div class="form-group">
          <label for="password">密码：</label>
          <input 
            :type="showPassword ? 'text' : 'password'" 
            id="password" 
            v-model="formData.password" 
            @input="validatePassword"
            placeholder="请输入密码"
          />
          <button 
            type="button" 
            class="toggle-password"
            @click="togglePasswordVisibility"
          >
            {{ showPassword ? '隐藏' : '显示' }}
          </button>
          <span class="error-message" v-if="errors.password">{{ errors.password }}</span>
        </div>
  
        <div class="form-group">
          <label for="confirmPassword">确认密码：</label>
          <input 
            type="password" 
            id="confirmPassword" 
            v-model="formData.confirmPassword" 
            @input="validateConfirmPassword"
            placeholder="请再次输入密码"
          />
          <span class="error-message" v-if="errors.confirmPassword">{{ errors.confirmPassword }}</span>
        </div>
  
        <button type="submit" class="submit-btn" :disabled="!isFormValid">立即注册</button>
      </form>
  
      <div class="login-link">
        已有账号？<router-link to="/login">立即登录</router-link>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref, computed } from 'vue';
  import axios from 'axios';
  import { useRouter } from 'vue-router';
  
  const router = useRouter();
  // 获取用户信息
  const formData = ref({
    username: '',
    email: '',
    password: '',
    confirmPassword: ''
  })
  //
  const errors = ref({
    username: '',
    email: '',
    password: '',
    confirmPassword: ''
  })
  
  // 切换密码可见性
  const showPassword = ref(false)
  
  // 验证用户名
  const validateUsername = () => {
    if (!formData.value.username.trim()) {
      errors.value.username = '用户名不能为空'
    } else if (formData.value.username.length < 4) {
      errors.value.username = '用户名至少需要4个字符'
    } else {
      errors.value.username = ''
    }
  }
  
  // 验证邮箱
  const validateEmail = () => {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/
    if (!formData.value.email) {
      errors.value.email = '邮箱不能为空'
    } else if (!emailRegex.test(formData.value.email)) {
      errors.value.email = '请输入有效的邮箱地址'
    } else {
      errors.value.email = ''
    }
  }
  
  // 验证密码
  const validatePassword = () => {
    if (!formData.value.password) {
      errors.value.password = '密码不能为空'
    } else if (formData.value.password.length < 6) {
      errors.value.password = '密码至少需要6个字符'
    } else {
      errors.value.password = ''
    }
  }
  // 验证确认密码
  const validateConfirmPassword = () => {
    if (!formData.value.confirmPassword) {
      errors.value.confirmPassword = '请确认密码'
    } else if (formData.value.confirmPassword !== formData.value.password) {
      errors.value.confirmPassword = '两次输入的密码不一致'
    } else {
      errors.value.confirmPassword = ''
    }
  }
  // 验证表单是否有效
  const isFormValid = computed(() => {
    return (
      !errors.value.username &&
      !errors.value.email &&
      !errors.value.password &&
      !errors.value.confirmPassword &&
      formData.value.username &&
      formData.value.email &&
      formData.value.password &&
      formData.value.confirmPassword
    )
  })
  // 切换密码可见性
  const togglePasswordVisibility = () => {
    showPassword.value = !showPassword.value
  }
  // 提交表单,注册用户,发送请求,将用户信息发送到后端
  const handleSubmit = async () => {
  console.log('注册数据：', formData.value);
  try {
    //查看formData.value
    console.log('注册数据：', formData.value);
    // 发送请求时使用 formData.value
    // 发送请求时使用 formData.value
    const response = await axios.post('http://localhost:5000/register', formData.value);
    console.log('注册成功:', response.data);

    if (response.status === 201) {
      console.log('注册成功:', response.data);
      router.push('/login'); // 注册成功后跳转到登录页面
      // 成功后重置表单
      formData.value = {
        username: '',
        email: '',
        password: '',
        confirmPassword: ''
      };
      
    }
  } catch (error) {
    const errorMsg = error.response?.data?.message || error.message;
    // console.error('错误:', errorMsg);
    alert(`错误: ${errorMsg}`);
  }
  };
  </script>
  
  <style scoped>
  .register-container {
    max-width: 400px;
    margin: 2rem auto;
    padding: 2rem;
    background-color: #f5f5f5;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  }
  
  h2 {
    text-align: center;
    color: #333;
    margin-bottom: 1.5rem;
  }
  
  .register-form {
    display: flex;
    flex-direction: column;
    gap: 1rem;
  }
  
  .form-group {
    display: flex;
    flex-direction: column;
    position: relative;
  }
  
  label {
    margin-bottom: 0.5rem;
    color: #666;
    font-weight: 500;
  }
  
  input {
    padding: 0.8rem;
    border: 1px solid #ddd;
    border-radius: 4px;
    font-size: 1rem;
  }
  
  input:focus {
    outline: none;
    border-color: #409eff;
    box-shadow: 0 0 0 2px rgba(64, 158, 255, 0.1);
  }
  
  .toggle-password {
    position: absolute;
    right: 10px;
    top: 55%;
    transform: translateY(-50%);
    background: none;
    border: none;
    color: #666;
    cursor: pointer;
    font-size: 0.8rem;
  }
  
  .submit-btn {
    background-color: #409eff;
    color: white;
    padding: 0.8rem;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    font-size: 1rem;
    margin-top: 1rem;
    transition: background-color 0.3s;
  }
  
  .submit-btn:hover:not(:disabled) {
    background-color: #66b1ff;
  }
  
  .submit-btn:disabled {
    background-color: #a0cfff;
    cursor: not-allowed;
  }
  
  .error-message {
    color: #f56c6c;
    font-size: 0.8rem;
    margin-top: 0.3rem;
    height: 1.2rem;
  }
  
  .login-link {
    text-align: center;
    margin-top: 1.5rem;
    color: #666;
  }
  
  .login-link a {
    color: #409eff;
    text-decoration: none;
  }
  
  .login-link a:hover {
    text-decoration: underline;
  }
  </style>