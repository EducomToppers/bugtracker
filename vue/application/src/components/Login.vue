<template>
  <div class="container">
    <form @submit="submit_login" method="post">
      <div class="form-group">
        <label for="username">Username</label>
        <input type="text" id="username" class="form-control" :class="username_is_invalid" name="username" v-model="username">
        <span v-if="!hide_username_error" class="help-block">Username was not found</span>
      </div>
      <div class="form-group">
        <label for="password">Password</label>
        <input class="form-control" :class="password_is_invalid" type="password" id="password" name="password" v-model="password">
        <span v-if="!hide_password_error" class="help-block">Incorrect Password</span>
      </div>
      <button type="submit" class="btn btn-primary">Log in</button>
    </form>
    <a class="btn-signup" href="/accounts/register">No account?, click here to register</a>
  </div>
</template>

<script>
  export default {
    data() {
      return {
        username:'',
        password: '',
        hide_username_error: true,
        username_is_invalid: '',
        hide_password_error: true,
        password_is_invalid: ''
      };
    },
    methods: {
      async submit_login(e) {
        e.preventDefault();
        const axios = require('axios');
        const payload = {
          username: this.username,
          password: this.password
        }
          const response = await axios.post("accounts/login/", payload)
            .catch(error => {
              if (error.response.status === 400) {
                if (Object.keys(error.response.data).find(e => e === 'Not found')) {
                  this.username_is_invalid = 'is-invalid';
                  this.hide_username_error = false;
                  this.hide_password_error = true;
                } else if (Object.keys(error.response.data).find(e === 'Incorrect password')) {
                  this.hide_username_error = true;
                  this.hide_password_error = false;
                  this.is_password_error = 'is-invalid';
              }
            }
          });
          if (response && response.status === 200) {
            localStorage.setItem('user', JSON.stringify(response.data));
            this.$router.push('/');
            this.$router.go('/');
          }
      }
    }
  }
</script>
<style scoped>
  .btn.btn-primary {
    margin-top: 20px;
  }
  .help-block {
    color: red;
  }
  .btn-signup {
    margin-top: 20px;
  }
</style>
