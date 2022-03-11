<template>
    <div style="display: flex;
    flex-direction: row;
    gap: 2em;
    flex-wrap: wrap;
    ">
        <Product
            v-for="product of products" :key="product.id"
            v-bind:product="product"
        />
    </div>
</template>

<script>
import Product from '@/components/Product'
export default {
    props: ['products'],
    components: {
        Product
    }
}
</script>
