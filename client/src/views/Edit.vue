<template v-if="product != null">
    <div class="container w-50 p-3">
        <h3>Edit product</h3>
        <form  v-on:submit.prevent="updateForm">
            <div class="form-group">
                <label for="name">Name</label>
                <input type="text"  class="form-control" id="name" v-model="product.name">
            </div>
            <div class="form-group">
                <label for="price">price</label>
                <input type="text"  class="form-control" id="price" v-model="product.price">
            </div>
            <div class="form-group">
                <label for="author">Author</label>
                <input type="text"  class="form-control" id="author" v-model="product.author">
            </div>
            <div class="form-group mt-2">
                <div class="input-group-prepend">
                    <span class="input-group-text">Description</span>
                </div>
                <textarea class="form-control" aria-label="With textarea" id="description" v-model="product.description"></textarea>
            </div>
            <hr />
            <div class="form-group">
                <button type="submit" class="btn btn-primary">Update product</button>
            </div>
        </form>
        <h3 class="mt-2">Edit images</h3>
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
                <div class="card-body">
                    <button class="btn btn-danger" v-on:click="deleteImage(img.id)">Delete image</button>
                </div>
            </div>
        </div>
        <form  v-on:submit.prevent="updateImage(product.id)">
            <div class="form-group">
                <input type="file"  class="form-control" id="images" v-on:change="uploadFile" >
            </div>
            <hr />
            <div class="form-group">
                <button type="submit"  class="btn btn-primary">Update photo</button>
            </div>
        </form>
    </div>
</template>

<script>
import axios from 'axios';
export default {
  name: 'CreateForm',
    computed: {
        productId () {
            return +this.$route.params.id;
        }
    },

    data() {
        return {
            product: {},
            files: null,
        }
    },

    mounted() {
        this.getProduct()
    },

    updated() {
        document.getElementById('images').value = ''
    },

    methods: {
        async getProduct() {
            await fetch('http://127.0.0.1:8000/api/v1/product_detail/' + this.productId)
            .then(response => response.json())
            .then(json => {
            this.product = json})
        },

        uploadFile (event) {
            this.files = event.target.files[0]
        },

        async deleteImage(id) {
            await axios.delete('http://127.0.0.1:8000/api/v1/image_delete/' + id)
            .then(() => {
            this.getProduct()
            })
        },

        async updateImage(productId) {
            const data = new FormData();
            data.append('product', productId)
            data.append('image', this.files)
            console.log(data)
            await axios.post('http://127.0.0.1:8000/api/v1/image_create', data)
            .then(() => {
            this.getProduct()
            })
        },

        async updateForm()  {
            const data = new FormData();
            data.append('name', this.product.name)
            data.append('price', this.product.price)
            data.append('author', this.product.author)
            data.append('description', this.product.description)
            await axios.put('http://127.0.0.1:8000/api/v1/product_update/' + this.productId, data)
        }
    },
}
</script>