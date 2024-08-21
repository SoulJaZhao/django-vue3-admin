<template>
    <div class="home-container">
        <e-full-screen-container type="full">
            <n-grid :x-gap="24" :y-gap="24" :cols="3">
                <n-grid-item span="3">
                    <div class="grid-container">
                        <e-dynamic-text id="title" text="同济大学物联网边缘节点入侵检测平台" :colors="['#f53f3f', '#1e80ff']" />
                    </div>
                </n-grid-item>
                <n-grid-item>
                    <div class="grid-container">
                        <e-border-box-3 class="header-box" text="节点总览" font-color="#2d608d">
                            <n-grid x-gap="24" y-gap="8" :cols="4">
                                <n-gi class="gi-center">
                                    <label class="title-label" style="color: #4faebd;">节点总数</label>
                                </n-gi>
                                <n-gi class="gi-center">
                                    <label class="title-label" style="color: #6fff98;">在线节点</label>
                                </n-gi>
                                <n-gi class="gi-center">
                                    <label class="title-label" style="color: #f1c857;">离线节点</label>
                                </n-gi>
                                <n-gi class="gi-center">
                                    <label class="title-label" style="color: #e44079;">故障节点</label>
                                </n-gi>
                                <n-gi class="gi-center">
                                    <e-digital-flop font-size="40" color="#4faebd" :value="8129" :separator="','" />
                                </n-gi>
                                <n-gi class="gi-center">
                                    <e-digital-flop font-size="40" color="#6fff98" :value="7129" :separator="','" />
                                </n-gi>
                                <n-gi class="gi-center">
                                    <e-digital-flop font-size="40" color="#f1c857" :value="518" :separator="','" />
                                </n-gi>
                                <n-gi class="gi-center">
                                    <e-digital-flop font-size="40" color="#e44079" :value="482" :separator="','" />
                                </n-gi>
                            </n-grid>
                        </e-border-box-3>
                    </div>
                </n-grid-item>
                <n-grid-item>
                    <div class="grid-container">
                        <e-border-box-3 class="header-box" text="E-DataV 边框">
                        </e-border-box-3>
                    </div>
                </n-grid-item>
                <n-grid-item>
                    <div class="grid-container">
                        <e-border-box-3 class="header-box" text="E-DataV 边框">
                        </e-border-box-3>
                    </div>
                </n-grid-item>
            </n-grid>
        </e-full-screen-container>
    </div>
</template>

<style scoped>
#title {
    font-size: 40px;
    font-weight: bold;
}

.title-label {
    font-size: 25px;
    margin-top: 20px;
    color: #fff;
    font-weight: bold;
}

.home-container {
    width: 100%;
    height: 100%;
    padding: 16px 16px 10px 16px;
    box-sizing: border-box;
    background-image: url(./resource/background.png);
    background-size: cover;
    background-position: 50%;
}

.header-container {
    display: flex;
    justify-content: center;
    align-items: center;
    width: 100%;
    margin: 10px;
}

.grid-container {
    display: flex;
    justify-content: center;
    align-items: center;
}

.gi-center {
    display: flex;
    justify-content: center;
    align-items: center;
}

.header-box {
    width: 100%;
    margin: 10px;
}
</style>

<script lang="ts">
import { defineComponent } from 'vue';
import { NGrid, NGi, NGridItem, NRow, NCol, NStatistic, NGradientText } from 'naive-ui';
import { EFullScreenContainer, EBorderBox3, EDynamicText, EDigitalFlop } from 'e-datav-vue3';
import { Decoration11 } from '@kjgl77/datav-vue3';

export default defineComponent({
    name: 'home',
    components: {
        NGrid,
        NGi,
        NRow,
        NCol,
        NStatistic,
        NGridItem,
        NGradientText,
        EFullScreenContainer,
        EBorderBox3,
        EDynamicText,
        EDigitalFlop,
        Decoration11,
    }
});
</script>
