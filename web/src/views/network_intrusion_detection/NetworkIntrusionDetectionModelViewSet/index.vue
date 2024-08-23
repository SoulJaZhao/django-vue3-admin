<template>
    <el-row>
        <el-col :span="24">
            <el-card class="card-itme">
                <el-row>
                    <el-col :span="24" justify="center" align="center">
                        <el-text class="mx-1" tag="b" size="large">今日网络入侵告警事件</el-text>
                    </el-col>
                </el-row>
                <el-row>
                    <!-- 总数 -->
                    <el-col :span="2" justify="center" align="center">
                        <el-row>
                            <el-col :span="24">
                                <e-digital-flop font-size="50" :value="1320" color="#007bff" />
                            </el-col>
                        </el-row>
                        <el-row>
                            <el-col :span="24">
                                <el-text class="mx-1" tag="b" size="large" style="color: #007bff;">总数</el-text>
                            </el-col>
                        </el-row>
                    </el-col>

                    <!-- 后门攻击 -->
                    <el-col :span="2" justify="center" align="center">
                        <el-row>
                            <el-col :span="24">
                                <e-digital-flop font-size="50" :value="400" color="#28a745" />
                            </el-col>
                        </el-row>
                        <el-row>
                            <el-col :span="24">
                                <el-text class="mx-1" tag="b" size="large" style="color: #28a745;">后门攻击</el-text>
                            </el-col>
                        </el-row>
                    </el-col>

                    <!-- DoS攻击 -->
                    <el-col :span="2" justify="center" align="center">
                        <el-row>
                            <el-col :span="24">
                                <e-digital-flop font-size="50" :value="220" color="#dc3545" />
                            </el-col>
                        </el-row>
                        <el-row>
                            <el-col :span="24">
                                <el-text class="mx-1" tag="b" size="large" style="color: #dc3545;">DoS攻击</el-text>
                            </el-col>
                        </el-row>
                    </el-col>

                    <!-- DDoS攻击 -->
                    <el-col :span="2" justify="center" align="center">
                        <el-row>
                            <el-col :span="24">
                                <e-digital-flop font-size="50" :value="150" color="#6f42c1" />
                            </el-col>
                        </el-row>
                        <el-row>
                            <el-col :span="24">
                                <el-text class="mx-1" tag="b" size="large" style="color: #6f42c1;">DDoS攻击</el-text>
                            </el-col>
                        </el-row>
                    </el-col>

                    <!-- SQL注入攻击 -->
                    <el-col :span="2" justify="center" align="center">
                        <el-row>
                            <el-col :span="24">
                                <e-digital-flop font-size="50" :value="110" color="#fd7e14" />
                            </el-col>
                        </el-row>
                        <el-row>
                            <el-col :span="24">
                                <el-text class="mx-1" tag="b" size="large" style="color: #fd7e14;">SQL注入攻击</el-text>
                            </el-col>
                        </el-row>
                    </el-col>

                    <!-- 中间人攻击 -->
                    <el-col :span="2" justify="center" align="center">
                        <el-row>
                            <el-col :span="24">
                                <e-digital-flop font-size="50" :value="80" color="#17a2b8" />
                            </el-col>
                        </el-row>
                        <el-row>
                            <el-col :span="24">
                                <el-text class="mx-1" tag="b" size="large" style="color: #17a2b8;">中间人攻击</el-text>
                            </el-col>
                        </el-row>
                    </el-col>

                    <!-- 密码攻击 -->
                    <el-col :span="2" justify="center" align="center">
                        <el-row>
                            <el-col :span="24">
                                <e-digital-flop font-size="50" :value="100" color="#ffc107" />
                            </el-col>
                        </el-row>
                        <el-row>
                            <el-col :span="24">
                                <el-text class="mx-1" tag="b" size="large" style="color: #ffc107;">密码攻击</el-text>
                            </el-col>
                        </el-row>
                    </el-col>

                    <!-- 勒索病毒 -->
                    <el-col :span="2" justify="center" align="center">
                        <el-row>
                            <el-col :span="24">
                                <e-digital-flop font-size="50" :value="120" color="#795548" />
                            </el-col>
                        </el-row>
                        <el-row>
                            <el-col :span="24">
                                <el-text class="mx-1" tag="b" size="large" style="color: #795548;">勒索病毒</el-text>
                            </el-col>
                        </el-row>
                    </el-col>

                    <!-- 扫描攻击 -->
                    <el-col :span="2" justify="center" align="center">
                        <el-row>
                            <el-col :span="24">
                                <e-digital-flop font-size="50" :value="90" color="#343a40" />
                            </el-col>
                        </el-row>
                        <el-row>
                            <el-col :span="24">
                                <el-text class="mx-1" tag="b" size="large" style="color: #343a40;">扫描攻击</el-text>
                            </el-col>
                        </el-row>
                    </el-col>

                    <!-- 命令注入 -->
                    <el-col :span="2" justify="center" align="center">
                        <el-row>
                            <el-col :span="24">
                                <e-digital-flop font-size="50" :value="50" color="#6c757d" />
                            </el-col>
                        </el-row>
                        <el-row>
                            <el-col :span="24">
                                <el-text class="mx-1" tag="b" size="large" style="color: #6c757d;">命令注入</el-text>
                            </el-col>
                        </el-row>
                    </el-col>

                    <!-- XSS攻击 -->
                    <el-col :span="2" justify="center" align="center">
                        <el-row>
                            <el-col :span="24">
                                <e-digital-flop font-size="50" :value="60" color="#28a745" />
                            </el-col>
                        </el-row>
                        <el-row>
                            <el-col :span="24">
                                <el-text class="mx-1" tag="b" size="large" style="color: #28a745;">XSS攻击</el-text>
                            </el-col>
                        </el-row>
                    </el-col>

                    <!-- APT攻击 -->
                    <el-col :span="2" justify="center" align="center">
                        <el-row>
                            <el-col :span="24">
                                <e-digital-flop font-size="50" :value="40" color="#dc3545" />
                            </el-col>
                        </el-row>
                        <el-row>
                            <el-col :span="24">
                                <el-text class="mx-1" tag="b" size="large" style="color: #dc3545;">APT攻击</el-text>
                            </el-col>
                        </el-row>
                    </el-col>
                </el-row>
            </el-card>
        </el-col>
    </el-row>
</template>

<script lang="ts">
import { onMounted, defineComponent } from 'vue';
import * as echarts from 'echarts';
import { EDigitalFlop } from 'e-datav-vue3';

export default defineComponent({
    name: "NetworkIntrusionDetectionModelViewSet",
    components: {
        EDigitalFlop,
    },
    setup() {
        onMounted(() => {

        });

        return {

        };
    },
});
</script> 

<style scoped lang="scss">
.card-item {
    width: 100%;
    min-height: 180px;
    overflow: hidden;
    padding: 20px;
}
</style>