<template>
<div class="container">
  <div class="d-flex flex-wrap justify-content-center my-3">
    <div class="col-md-8 blog-main">
      <div class="blog-post">
        <h2 class="blog-post-title">{{product.name}}</h2>
        <p class="blog-post-meta text-secondary">{{product.time_created}}</p>
        <p class="blog-post-meta text-secondary">Created buy <strong>{{product.author}}</strong></p>
        <div class="form-group">
          <div class="input-group-prepend">
            <span class="input-group-text"><strong>Description</strong></span>
          </div>
          <div class="form-control"><p>aboba</p></div>
        </div>
        <hr>
        <div class="form-group">
          <div class="input-group-prepend">
              <span class="input-group-text"><strong>Images</strong></span>
          </div>
          <div 
          style="display: flex;
          flex-direction: row;
          gap: 2em;
          flex-wrap: wrap;
          ">
            <div class="card" v-for="img of product.productimage_set" :key="img" style="width: 12rem; margin-bottom: 2em; padding: 1em;">
              <div>
                  <img :src="`${img.image}`"  class="card-img-top" alt="...">
              </div>
            </div>
          </div>
        </div>
        <hr>
        <router-link class="btn btn-primary" :to="linkOpen">Edit</router-link>
        <button class="btn btn-danger" style="margin-left: 1em;" v-on:click="Delete">Delete</button>
      </div><!-- /.blog-post -->
    </div>
  </div><!-- /.blog-main -->
</div>
</template>
    
<script>
export default {
  computed: {
    productId () {
        return +this.$route.params.id;
    },

    linkOpen () {
        return `/edit/${this.product.id}`;
    }
  },

  data() {
    return {
    product: {}
    }       
  },

  methods: {
    async Delete() {
      await fetch('http://127.0.0.1:8000/api/v1/product_delete/' + this.productId, {
        method: 'DELETE',
        headers: {
        'Content-type': 'application/json; charset=UTF-8',
        },
      })
      this.$router.push('/')
    }
  },

  mounted() {
    fetch('http://127.0.0.1:8000/api/v1/product_detail/' + this.productId)
    .then(response => response.json())
    .then(json => {
    this.product = json
    })
  },
}
</script>