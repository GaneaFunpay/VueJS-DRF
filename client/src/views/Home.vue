<template class="text-center">
  <div class="container mt-3 content-center">
    <ProductList
      v-bind:products="products" 
    />
    <template v-if="showNextButton">
      <button class="btn btn-primary" @click="loadNext()">Next</button>
    </template>
    <template v-if="showPrevButton">
      <button class="btn btn-primary" @click="loadPrev()">Last</button>
    </template>
  </div>
</template>

<script>
import ProductList from '@/components/ProductList';
export default {
  data() {
    return {
      products: [],
      currentPage: 1,
      showNextButton: false,
      showPrevButton: false
    }
  },

  delimiters: ['[[', ']]'],

  mounted() {
    this.getProducts()  
  },

  methods: {
    loadNext() {
      this.currentPage += 1
      this.getProducts()
    },

    loadPrev() {
      this.currentPage -= 1
      this.getProducts()
    },

    async getProducts() {
      await fetch(`http://127.0.0.1:8000/api/v1/product/?page=${this.currentPage}`)
        .then(response =>{return response.json()})
        .then(data => {
          this.showNextButton = false
          this.showPrevButton = false

          if (data.next) {
            this.showNextButton = true
          }

          if (data.previous) {
            this.showPrevButton = true
          }

          this.products = data.results
        })
        .catch(error => {
          console.log(error)
        })
    }
  },
  
  components: {
    ProductList
  }
}
</script>