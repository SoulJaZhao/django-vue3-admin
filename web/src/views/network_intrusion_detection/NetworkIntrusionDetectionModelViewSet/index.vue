<template>
  <div>
    <el-row class="mb-15">
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
                  <el-text class="mx-1" tag="b" size="large" style="color: #007bff">总数</el-text>
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
                  <el-text class="mx-1" tag="b" size="large" style="color: #28a745">后门攻击</el-text>
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
                  <el-text class="mx-1" tag="b" size="large" style="color: #dc3545">DoS攻击</el-text>
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
                  <el-text class="mx-1" tag="b" size="large" style="color: #6f42c1">DDoS攻击</el-text>
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
                  <el-text class="mx-1" tag="b" size="large" style="color: #fd7e14">SQL注入攻击</el-text>
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
                  <el-text class="mx-1" tag="b" size="large" style="color: #17a2b8">中间人攻击</el-text>
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
                  <el-text class="mx-1" tag="b" size="large" style="color: #ffc107">密码攻击</el-text>
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
                  <el-text class="mx-1" tag="b" size="large" style="color: #795548">勒索病毒</el-text>
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
                  <el-text class="mx-1" tag="b" size="large" style="color: #343a40">扫描攻击</el-text>
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
                  <el-text class="mx-1" tag="b" size="large" style="color: #6c757d">命令注入</el-text>
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
                  <el-text class="mx-1" tag="b" size="large" style="color: #28a745">XSS攻击</el-text>
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
                  <el-text class="mx-1" tag="b" size="large" style="color: #dc3545">APT攻击</el-text>
                </el-col>
              </el-row>
            </el-col>
          </el-row>
        </el-card>
      </el-col>
    </el-row>
    <el-row gutter="15" class="mb-15">
      <el-col :span="12">
        <el-card class="card-item">
          <div ref="totalChartRef" style="width: 100%; height: 320px"></div>
        </el-card>
      </el-col>
      <el-col :span="12">
        <el-card class="card-item">
          <div ref="heatmapChartRef" style="width: 100%; height: 320px"></div>
        </el-card>
      </el-col>
    </el-row>
    <el-row gutter="15" class="mb-15">
      <el-col :span="5">
        <el-card class="card-item">
          <el-text class="mx-1" tag="b" size="large">告警处理进度</el-text>
          <el-progress :text-inside="true" :stroke-width="25" :percentage="31" status="exception" striped striped-flow
            :duration="10" class="mt-15">
            <span>后门攻击 31%</span>
          </el-progress>
          <el-progress :text-inside="true" :stroke-width="22" :percentage="41" status="exception" striped striped-flow
            :duration="10" class="mt-15">
            <span>DoS攻击 41%</span>
          </el-progress>
          <el-progress :text-inside="true" :stroke-width="25" :percentage="61" status="warning" striped striped-flow
            :duration="10" class="mt-15">
            <span>DDoS攻击 61%</span>
          </el-progress>
          <el-progress :text-inside="true" :stroke-width="25" :percentage="71" status="warning" striped striped-flow
            :duration="10" class="mt-15">
            <span>SQL注入攻击 71%</span>
          </el-progress>
          <el-progress :text-inside="true" :stroke-width="25" :percentage="91" striped striped-flow :duration="10"
            status="successful" class="mt-15">
            <span>中间人攻击 91%</span>
          </el-progress>
          <el-progress :text-inside="true" :stroke-width="25" :percentage="95" striped striped-flow :duration="10"
            status="success" class="mt-15">
            <span>密码攻击 95%</span>
          </el-progress>
          <el-progress :text-inside="true" :stroke-width="25" :percentage="97" striped striped-flow :duration="10"
            status="success" class="mt-15">
            <span>勒索病毒 97%</span>
          </el-progress>
        </el-card>
      </el-col>
      <el-col :span="6">
        <el-card class="card-item">
          <el-text class="mx-1" tag="b" size="large">模型效果</el-text>
          <el-row class="mt-15">
            <el-col :span="12" justify="center" align="center">
              <el-progress type="dashboard" stroke-width="10" stroke-color="#fff" :percentage="97">
                <template #default="{ percentage }">
                  <span class="percentage-value" style="color: #409eff">{{ percentage }}%</span>
                  <span class="percentage-label" style="color: #409eff">精确率</span>
                </template>
              </el-progress>
            </el-col>
            <el-col :span="12" justify="center" align="center">
              <el-progress type="dashboard" stroke-width="10" :percentage="98" status="success">
                <template #default="{ percentage }">
                  <span class="percentage-value">{{ percentage }}%</span>
                  <span class="percentage-label">召回率</span>
                </template>
              </el-progress>
            </el-col>
            <el-col :span="12" justify="center" align="center">
              <el-progress type="dashboard" stroke-width="10" :percentage="98" status="warning">
                <template #default="{ percentage }">
                  <span class="percentage-value">{{ percentage }}%</span>
                  <span class="percentage-label">准确率</span>
                </template>
              </el-progress>
            </el-col>
            <el-col :span="12" justify="center" align="center">
              <el-progress type="dashboard" stroke-width="10" :percentage="97" status="exception">
                <template #default="{ percentage }">
                  <span class="percentage-value">{{ percentage }}%</span>
                  <span class="percentage-label">F1得分</span>
                </template>
              </el-progress>
            </el-col>
          </el-row>
        </el-card>
      </el-col>
      <el-col :span="13" justify="center" align="center">
        <el-card class="card-item">
          <div ref="gradientChartRef" style="width: 100%; height: 305px"></div>
        </el-card>
      </el-col>
    </el-row>
    <el-row gutter="15" class="mb-15">
      <el-col :span="12" justify="center" align="center">
        <el-card class="card-item">
          <el-row>
            <el-col :span="8" justify="center" align="center">
              <e-digital-flop font-size="50" :value="12" color="#007bff" />
            </el-col>
            <el-col :span="8" justify="center" align="center">
              <e-digital-flop font-size="50" :value="4" color="#E6A23C" />
            </el-col>
            <el-col :span="8" justify="center" align="center">
              <e-digital-flop font-size="50" :value="5" color="#F56C6C" />
            </el-col>
          </el-row>
          <el-row>
            <el-col :span="8" justify="center" align="center">
              <el-text class="mx-1" tag="b" size="large" style="color: #007bff">在线节点</el-text>
            </el-col>
            <el-col :span="8" justify="center" align="center">
              <el-text class="mx-1" tag="b" size="large" style="color: #E6A23C">离线节点</el-text>
            </el-col>
            <el-col :span="8" justify="center" align="center">
              <el-text class="mx-1" tag="b" size="large" style="color: #F56C6C">故障节点</el-text>
            </el-col>
          </el-row>
        </el-card>
      </el-col>
      <el-col :span="12" justify="center" align="center">
        <el-card class="card-item">
          <el-row>
            <el-col :span="6" justify="center" align="center">
              <e-water-level-pond :waveColors="['#007bff', '#b0e0ff']" duration="0" style="width:80px;height:80px;"
                :value="86" />
            </el-col>
            <el-col :span="6" justify="center" align="center">
              <e-water-level-pond :waveColors="['#E6A23C', '#b0e0ff']" duration="0" style="width:80px;height:80px;"
                :value="95" />
            </el-col>
            <el-col :span="6" justify="center" align="center">
              <e-water-level-pond :waveColors="['#F56C6C', '#b0e0ff']" duration="0" style="width:80px;height:80px;"
                :value="90" />
            </el-col>
            <el-col :span="6" justify="center" align="center">
              <e-water-level-pond :waveColors="[' #67C23A', '#b0e0ff']" duration="0" style="width:80px;height:80px;"
                :value="81" />
            </el-col>
          </el-row>
          <el-row class="mt-15">
            <el-col :span="6" justify="center" align="center">
              <el-text class="mx-1" tag="b" size="large" style="color: #007bff">CPU平均负载</el-text>
            </el-col>
            <el-col :span="6" justify="center" align="center">
              <el-text class="mx-1" tag="b" size="large" style="color: #E6A23C">GPU平均负载</el-text>
            </el-col>
            <el-col :span="6" justify="center" align="center">
              <el-text class="mx-1" tag="b" size="large" style="color: #F56C6C">内存平均负载</el-text>
            </el-col>
            <el-col :span="6" justify="center" align="center">
              <el-text class="mx-1" tag="b" size="large" style="color: #67C23A">磁盘平均负载</el-text>
            </el-col>
          </el-row>
        </el-card>
      </el-col>
    </el-row>
    <el-row gutter="15" class="mb-15">
      <el-col :span="6" justify="center" align="center">
        <el-card class="card-item">
          <el-text class="mx-1" tag="b" size="large">CPU负载情况</el-text>
          <el-progress :text-inside="true" :stroke-width="25" :percentage="97" class="mt-15">
            <span>上海节点01 97%</span>
          </el-progress>
          <el-progress :text-inside="true" :stroke-width="25" :percentage="96" class="mt-15">
            <span>北京节点01 95%</span>
          </el-progress>
          <el-progress :text-inside="true" :stroke-width="25" :percentage="98" class="mt-15">
            <span>广州节点01 98%</span>
          </el-progress>
          <el-progress :text-inside="true" :stroke-width="25" :percentage="97" class="mt-15">
            <span>深圳节点01 97%</span>
          </el-progress>
          <el-progress :text-inside="true" :stroke-width="25" :percentage="92" class="mt-15">
            <span>杭州节点01 92%</span>
          </el-progress>
          <el-progress :text-inside="true" :stroke-width="25" :percentage="96" class="mt-15">
            <span>武汉节点01 96%</span>
          </el-progress>
        </el-card>
      </el-col>
      <el-col :span="6" justify="center" align="center">
        <el-card class="card-item">
          <el-text class="mx-1" tag="b" size="large">GPU负载情况</el-text>
          <el-progress :text-inside="true" :stroke-width="25" :percentage="97" status="warning" class="mt-15">
            <span>上海节点01 97%</span>
          </el-progress>
          <el-progress :text-inside="true" :stroke-width="25" :percentage="96" status="warning" class="mt-15">
            <span>北京节点01 95%</span>
          </el-progress>
          <el-progress :text-inside="true" :stroke-width="25" :percentage="98" status="warning" class="mt-15">
            <span>广州节点01 98%</span>
          </el-progress>
          <el-progress :text-inside="true" :stroke-width="25" :percentage="97" status="warning" class="mt-15">
            <span>深圳节点01 97%</span>
          </el-progress>
          <el-progress :text-inside="true" :stroke-width="25" :percentage="92" status="warning" class="mt-15">
            <span>杭州节点01 92%</span>
          </el-progress>
          <el-progress :text-inside="true" :stroke-width="25" :percentage="96" status="warning" class="mt-15">
            <span>武汉节点01 96%</span>
          </el-progress>
        </el-card>
      </el-col>
      <el-col :span="6" justify="center" align="center">
        <el-card class="card-item">
          <el-text class="mx-1" tag="b" size="large">内存负载情况</el-text>
          <el-progress :text-inside="true" :stroke-width="25" :percentage="97" status="success" class="mt-15">
            <span>上海节点01 97%</span>
          </el-progress>
          <el-progress :text-inside="true" :stroke-width="25" :percentage="96" status="success" class="mt-15">
            <span>北京节点01 95%</span>
          </el-progress>
          <el-progress :text-inside="true" :stroke-width="25" :percentage="98" status="success" class="mt-15">
            <span>广州节点01 98%</span>
          </el-progress>
          <el-progress :text-inside="true" :stroke-width="25" :percentage="97" status="success" class="mt-15">
            <span>深圳节点01 97%</span>
          </el-progress>
          <el-progress :text-inside="true" :stroke-width="25" :percentage="92" status="success" class="mt-15">
            <span>杭州节点01 92%</span>
          </el-progress>
          <el-progress :text-inside="true" :stroke-width="25" :percentage="96" status="success" class="mt-15">
            <span>武汉节点01 96%</span>
          </el-progress>
        </el-card>
      </el-col>
      <el-col :span="6" justify="center" align="center">
        <el-card class="card-item">
          <el-text class="mx-1" tag="b" size="large">磁盘负载情况</el-text>
          <el-progress :text-inside="true" :stroke-width="25" :percentage="97" status="exception" class="mt-15">
            <span>上海节点01 97%</span>
          </el-progress>
          <el-progress :text-inside="true" :stroke-width="25" :percentage="96" status="exception" class="mt-15">
            <span>北京节点01 95%</span>
          </el-progress>
          <el-progress :text-inside="true" :stroke-width="25" :percentage="98" status="exception" class="mt-15">
            <span>广州节点01 98%</span>
          </el-progress>
          <el-progress :text-inside="true" :stroke-width="25" :percentage="97" status="exception" class="mt-15">
            <span>深圳节点01 97%</span>
          </el-progress>
          <el-progress :text-inside="true" :stroke-width="25" :percentage="92" status="exception" class="mt-15">
            <span>杭州节点01 92%</span>
          </el-progress>
          <el-progress :text-inside="true" :stroke-width="25" :percentage="96" status="exception" class="mt-15">
            <span>武汉节点01 96%</span>
          </el-progress>
        </el-card>
      </el-col>
    </el-row>
    <el-row :gutter="15">
      <el-col :span="6" justify="center" align="center">
        <el-card class="card-item">
          <el-text class="mx-1" tag="b" size="large">模型效果</el-text>
          <el-row class="mt-15">
            <el-col :span="12" justify="center" align="center">
              <el-progress type="dashboard" stroke-width="10" stroke-color="#fff" :percentage="97">
                <template #default="{ percentage }">
                  <span class="percentage-value" style="color: #409eff">{{ percentage }}%</span>
                  <span class="percentage-label" style="color: #409eff">精确率</span>
                </template>
              </el-progress>
            </el-col>
            <el-col :span="12" justify="center" align="center">
              <el-progress type="dashboard" stroke-width="10" :percentage="98" status="success">
                <template #default="{ percentage }">
                  <span class="percentage-value">{{ percentage }}%</span>
                  <span class="percentage-label">召回率</span>
                </template>
              </el-progress>
            </el-col>
            <el-col :span="12" justify="center" align="center">
              <el-progress type="dashboard" stroke-width="10" :percentage="98" status="warning">
                <template #default="{ percentage }">
                  <span class="percentage-value">{{ percentage }}%</span>
                  <span class="percentage-label">准确率</span>
                </template>
              </el-progress>
            </el-col>
            <el-col :span="12" justify="center" align="center">
              <el-progress type="dashboard" stroke-width="10" :percentage="97" status="exception">
                <template #default="{ percentage }">
                  <span class="percentage-value">{{ percentage }}%</span>
                  <span class="percentage-label">F1得分</span>
                </template>
              </el-progress>
            </el-col>
          </el-row>
        </el-card>
      </el-col>
      <el-col :span="8" justify="center" align="center">
        <el-card class="card-item">
          <div ref="barChartRef" style="width: 100%; height: 300px"></div>
        </el-card>
      </el-col>
      <el-col :span="10" justify="center" align="center">
        <el-card class="card-item">
          <div ref="lineChartRef" style="width: 100%; height: 300px"></div>
        </el-card>
      </el-col>
    </el-row>
  </div>
</template>

<script lang="ts">
import {
  onMounted,
  onBeforeUnmount,
  onActivated,
  defineComponent,
  ref,
} from "vue";
import * as echarts from "echarts";
import { EDigitalFlop, EWaterLevelPond } from "e-datav-vue3";

export default defineComponent({
  name: "NetworkIntrusionDetectionModelViewSet",
  components: {
    EDigitalFlop,
    EWaterLevelPond,
  },
  setup() {
    const totalChartRef = ref<HTMLDivElement | null>(null);
    const heatmapChartRef = ref<HTMLDivElement | null>(null);
    const gradientChartRef = ref<HTMLDivElement | null>(null);
    const barChartRef = ref<HTMLDivElement | null>(null);
    const lineChartRef = ref<HTMLDivElement | null>(null);

    let totalChart: echarts.ECharts | null = null;
    let heatmapChart: echarts.ECharts | null = null;
    let gradientChart: echarts.ECharts | null = null;
    let barChart: echarts.ECharts | null = null;
    let lineChart: echarts.ECharts | null = null;

    const initCharts = () => {
      if (totalChartRef.value) {
        if (totalChart) {
          totalChart.dispose();
        }
        totalChart = echarts.init(totalChartRef.value);
        const totalOption = {
          title: {
            text: "网络流量汇总",
            textStyle: {
              fontSize: 16, // 设置标题文字大小
            },
          },
          tooltip: {
            trigger: "axis",
          },
          legend: {
            data: ["入站流量", "出站流量"],
          },
          grid: {
            left: "3%",
            right: "4%",
            bottom: "3%",
            containLabel: true,
          },
          xAxis: {
            type: "category",
            boundaryGap: false,
            data: Array.from({ length: 10 }, (_, i) => `${i + 1}秒`),
          },
          yAxis: {
            type: "value",
          },
          series: [
            {
              name: "入站流量",
              type: "line",
              data: Array(10).fill(0),
            },
            {
              name: "出站流量",
              type: "line",
              data: Array(10).fill(0),
            },
          ],
        };
        totalChart.setOption(totalOption);

        setInterval(() => {
          const newInbound = Math.round(Math.random() * 100);
          const newOutbound = Math.round(Math.random() * 100);
          const newTime = new Date().toLocaleTimeString();

          totalOption.xAxis.data.shift();
          totalOption.xAxis.data.push(newTime);
          totalOption.series[0].data.shift();
          totalOption.series[0].data.push(newInbound);
          totalOption.series[1].data.shift();
          totalOption.series[1].data.push(newOutbound);

          totalChart?.setOption(totalOption);
        }, 1000);
      }
    };

    const initHeatmap = () => {
      if (heatmapChartRef.value) {
        if (heatmapChart) {
          heatmapChart.dispose();
        }
        heatmapChart = echarts.init(heatmapChartRef.value);

        const cities = ["北京", "上海", "广州", "深圳", "武汉"];
        const hosts = Array.from({ length: 5 }, (_, i) => `节点${i + 1}`);
        const data = [];

        for (let i = 0; i < cities.length; i++) {
          for (let j = 0; j < hosts.length; j++) {
            data.push([
              i,
              j,
              Math.round(Math.random() * 100), // 模拟流量数据
            ]);
          }
        }

        const heatmapOption = {
          title: {
            text: "节点流量热力图",
            textStyle: {
              fontSize: 16, // 设置标题文字大小
            },
          },
          tooltip: {
            position: "bottom",
          },
          grid: {
            left: "3%",
            right: "4%",
            bottom: "3%",
            containLabel: true,
          },
          xAxis: {
            type: "category",
            data: hosts,
            axisLabel: {
              interval: 0,
            },
          },
          yAxis: {
            type: "category",
            data: cities,
            inverse: true,
            axisLabel: {
              interval: 0,
            },
          },
          visualMap: {
            min: 0,
            max: 100,
            calculable: true,
            orient: "horizontal",
            left: "center",
            top: "0%",
          },
          series: [
            {
              name: "流量",
              type: "heatmap",
              data: data,
              label: {
                show: true,
                formatter: ({ value }) => `${value[2]}`,
              },
            },
          ],
        };

        heatmapChart.setOption(heatmapOption);
      }
    };

    const initGradientChart = () => {
      if (gradientChartRef.value) {
        if (gradientChart) {
          gradientChart.dispose();
        }
        gradientChart = echarts.init(gradientChartRef.value);

        // 模拟数据
        const days = ["周一", "周二", "周三", "周四", "周五", "周六", "周日"];
        const eventTypes = [
          "后门攻击",
          "DoS攻击",
          "DDoS攻击",
          "SQL注入攻击",
          "中间人攻击",
        ];
        const colors = ["#ff6f00", "#ffab00", "#f57f17", "#ff8f00", "#ff5722"];

        const generateRandomData = () =>
          Array.from({ length: 7 }, () => Math.round(Math.random() * 100));

        const seriesData = eventTypes.map((eventType, index) => ({
          name: eventType,
          type: "line",
          stack: "总量",
          areaStyle: {},
          emphasis: {
            focus: "series",
          },
          data: generateRandomData(),
          // 渐变色
          lineStyle: {
            width: 1,
            opacity: 0.5,
          },
          itemStyle: {
            color: colors[index],
          },
        }));

        const gradientChartOption = {
          title: {
            text: "本周告警事件统计",
            textStyle: {
              fontSize: 16,
            },
          },
          tooltip: {
            trigger: "axis",
          },
          legend: {
            data: eventTypes,
            show: false, // 隐藏图例
          },
          grid: {
            left: "3%",
            right: "4%",
            bottom: "3%",
            containLabel: true,
          },
          xAxis: {
            type: "category",
            data: days,
          },
          yAxis: {
            type: "value",
          },
          series: seriesData,
        };

        gradientChart.setOption(gradientChartOption);
      }
    };

    const initBarChart = () => {
      const chart = echarts.init(barChartRef.value);

      const options = {
        title: {
          text: '边缘节点负载异常事件',
          left: 'center'
        },
        tooltip: {
          trigger: 'axis',
          axisPointer: {
            type: 'shadow'
          }
        },
        legend: {
          data: ['异常事件数量'],
          bottom: '0'
        },
        grid: {
          left: '3%',
          right: '4%',
          bottom: '10%',
          containLabel: true
        },
        xAxis: {
          type: 'category',
          data: ['节点1', '节点2', '节点3', '节点4', '节点5'],  // 示例节点名称
          axisTick: {
            alignWithLabel: true
          }
        },
        yAxis: {
          type: 'value',
          name: '事件数量'
        },
        series: [
          {
            name: '异常事件数量',
            type: 'bar',
            barWidth: '60%',
            color: '#409EFF',
            data: [10, 15, 9, 20, 12]  // 示例数据，每个节点的异常事件数量
          }
        ]
      };

      chart.setOption(options);
    };

    const initLineChart = () => {
      const chart = echarts.init(lineChartRef.value);

      const options = {
        title: {
          text: '历史异常趋势',
          left: 'center'
        },
        tooltip: {
          trigger: 'axis'
        },
        legend: {
          data: ['异常事件数量'],
          bottom: '0'
        },
        grid: {
          left: '3%',
          right: '4%',
          bottom: '10%',
          containLabel: true
        },
        xAxis: {
          type: 'category',
          boundaryGap: false,
          data: ['2024-08-01', '2024-08-02', '2024-08-03', '2024-08-04', '2024-08-05', '2024-08-06', '2024-08-07'], // 示例日期
        },
        yAxis: {
          type: 'value',
          name: '事件数量'
        },
        series: [
          {
            name: '异常事件数量',
            type: 'line',
            data: [12, 15, 11, 13, 16, 10, 9], // 示例数据
            markPoint: {
              data: [
                { type: 'max', name: '最大值' },
                { type: 'min', name: '最小值' }
              ]
            },
            markLine: {
              data: [
                { type: 'average', name: '平均值' }
              ]
            }
          }
        ]
      };

      chart.setOption(options);

      // 如果需要在窗口大小改变时自动调整图表大小
      window.addEventListener('resize', () => {
        chart.resize();
      });
    };

    onMounted(() => {
      initCharts();
      initHeatmap();
      initGradientChart();
      initBarChart();
      initLineChart();
    });

    onActivated(() => {
      initCharts();
      initHeatmap();
      initGradientChart();
      initBarChart();
      initLineChart();
    });

    onBeforeUnmount(() => {
      if (totalChart) {
        totalChart.dispose();
      }

      if (heatmapChart) {
        heatmapChart.dispose();
      }

      if (gradientChart) {
        gradientChart.dispose();
      }

      if (barChart) {
        barChart.dispose();
      }

      if (lineChart) {
        lineChart.dispose();
      }
    });

    return {
      totalChartRef,
      heatmapChartRef,
      gradientChartRef,
      barChartRef,
      lineChartRef,
    };
  },
});
</script>

<style scoped lang="scss">
.mt-15 {
  margin-top: 15px;
}

.mb-15 {
  margin-bottom: 15px;
}

.card-item {
  width: 100%;
  min-height: 180px;
  overflow: hidden;
  padding: 10px;
}

.percentage-value {
  display: block;
  margin-top: 10px;
  font-size: 28px;
}

.percentage-label {
  display: block;
  margin-top: 10px;
  font-size: 15px;
}
</style>
