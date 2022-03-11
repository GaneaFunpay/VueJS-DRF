<template>
  <div id="nav">
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
      <a class="navbar-brand" >ProductTask</a>
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav">
          <li class="nav-item active">
            <router-link class="nav-link" to="/">Product list</router-link>
          </li>
          <li class="nav-item active">
            <router-link class="nav-link" to="/create">Create</router-link>
          </li>  
        </ul>
      </div>
    </nav>
  </div>
  <router-view />
</template>


<script>
export default {
  name: 'App'
}
</script>
