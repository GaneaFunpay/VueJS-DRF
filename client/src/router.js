import { createWebHistory, createRouter } from "vue-router";
import Create from "@/views/Create.vue";
import Home from "@/views/Home.vue";
import Details from "@/views/Details.vue";
import Edit from "@/views/Edit.vue";

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/create/",
    name: "Create",
    component: Create,
  },
  {
    path: "/details/:id",
    name: "Details",
    component: Details,
  },
  {
    path: "/edit/:id",
    name: "Edit",
    component: Edit,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;