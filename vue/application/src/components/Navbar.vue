<template>
<div>
    <header class="site-header">
      <nav class="navbar navbar-expand-md fixed-top">
        <div class="container">
          <div class="navbar-nav">
            <a v-if="!user_logged_in" class="nav-item nav-link" href="/accounts/register/">Register</a>
            <div v-if="user_logged_in" style="display: flex;">
            <a class="nav-item nav-link" href="#">Log out</a>
            <span style="padding: .5rem 1rem;">You are logged in as {{ username }}</span>
            </div>
            <router-link v-if="!user_logged_in" class="nav-item nav-link" to="/accounts/login/">Login</router-link>
          </div>
        </div>
      </nav>
    </header>
  </div>
</template>

<script>
export default {
  computed: {
      username() {
        const stored_user = JSON.parse(localStorage.getItem('user'));
        return stored_user ? stored_user.username : '';
      },
      user_logged_in() {
         return this.username? true: false
     }
  },
}
</script>
