<template>
    <div class="card" style="width: 18rem; ру margin-bottom: 2em; padding: 1em;">
        <div class=" px-0" v-if="product.productimage_set.length != 0">
            <img :src="product.productimage_set[0].image" class="card-img-top w-75 p-3" alt="...">
        </div>
    <div class="card-body">
        <h5 class="card-title">{{product.name}}</h5>
        <p class="card-text">{{product.price}} $</p>
        <router-link class="btn btn-primary" :to="linkOpen">Details</router-link>
    </div>
    </div>
</template>

<script>
export default {
    props: {
        product: {
            type: Object,
            required: true
        }
    },

    data() {
        return{
        }
    },

    computed: {
        linkOpen () {
            return `/details/${this.product.id}`;
        }
    }
}   
</script>