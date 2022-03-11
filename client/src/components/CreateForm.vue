<template>
<div class="container w-50 p-3">
  <h1>Create product</h1>
    <form  v-on:submit.prevent="submitForm">
      <div class="form-group">
          <label for="name">Name</label>
          <input type="text"  class="form-control" id="name" v-model="name">
      </div>
      <div class="form-group">
          <label for="price">Price</label>
          <input type="text"  class="form-control" id="price" v-model="price">
      </div>
      <div class="form-group">
          <label for="author">Author</label>
          <input type="text"  class="form-control" id="author" v-model="author">
      </div>
      <div class="form-group mt-2">
          <div class="input-group-prepend">
              <span class="input-group-text">Description</span>
          </div>
          <textarea class="form-control" aria-label="With textarea" id="description" v-model="description"></textarea>
      </div>
      <div class="form-group">
          <label for="">Photos</label>
            <input type="file"  class="form-control" id="images" v-on:change="uploadFile" multiple>
      </div>
      <hr />
      <div class="form-group">
        <button type="submit" class="btn btn-primary">Submit</button>
      </div>
  </form>
</div>    
</template>

<script>
import axios from 'axios';
export default {

  data() {
    return {
      name: '',
      price: '',
      author: '',
      description: '',
      files: null
    }
  },

  methods: {
     uploadFile (event) {
        this.files = event.target.files
        },

      async submitForm(){
        const data = new FormData();
        if (this.files != null){
          for (const i of Object.keys(this.files)) {
            data.append('images', this.files[i])
          }
        }
        data.append('name', this.name)
        data.append('price', this.price)
        data.append('author', this.author)
        data.append('description', this.description)
        await axios.post('http://127.0.0.1:8000/api/v1/product_create', data)
        .then((res) => {
            console.log(res)
          })
        this.$router.push('/')
    }
  },
}
</script>