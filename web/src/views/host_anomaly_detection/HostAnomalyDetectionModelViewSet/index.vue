<template>
    <div>
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
    name: "HostAnomalyDetectionModelViewSet",
    components: {
      EDigitalFlop,
      EWaterLevelPond,
    },
    setup() {
      const barChartRef = ref<HTMLDivElement | null>(null);
      const lineChartRef = ref<HTMLDivElement | null>(null);
  
      let barChart: echarts.ECharts | null = null;
      let lineChart: echarts.ECharts | null = null;
  
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
        initBarChart();
        initLineChart();
      });
  
      onActivated(() => {
        initBarChart();
        initLineChart();
      });
  
      onBeforeUnmount(() => {
        if (barChart) {
          barChart.dispose();
        }
  
        if (lineChart) {
          lineChart.dispose();
        }
      });
  
      return {
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
  